import assert from "node:assert/strict";
import { access, readFile, readdir } from "node:fs/promises";
import test from "node:test";

async function render() {
  const workerUrl = new URL("../dist/server/index.js", import.meta.url);
  workerUrl.searchParams.set("test", `${process.pid}-${Date.now()}`);
  const { default: worker } = await import(workerUrl.href);

  return worker.fetch(
    new Request("http://localhost/", {
      headers: { accept: "text/html" },
    }),
    {
      ASSETS: {
        fetch: async () => new Response("Not found", { status: 404 }),
      },
    },
    {
      waitUntil() {},
      passThroughOnException() {},
    },
  );
}

test("server-renders the AXIOM command surface", async () => {
  const response = await render();
  assert.equal(response.status, 200);
  assert.match(response.headers.get("content-type") ?? "", /^text\/html\b/i);

  const html = await response.text();
  assert.match(html, /<title>AXIOM — California Property Intelligence<\/title>/i);
  assert.match(html, /Order the/);
  assert.match(html, /PROPERTY INTELLIGENCE/);
  assert.match(html, /SYNTHETIC ENVIRONMENT/);
  assert.match(html, /Sacramento County Assessor/);
  assert.match(html, /CONNECTED REFERENCE BATCH/);
  assert.match(html, /Residential Dwelling Unit/);
  assert.match(html, /NO PARCEL, OWNER, OR MAILING RECORDS EXPOSED/);
  assert.match(html, /NEW BATCH DETECTED/);
  assert.match(html, /508,557/);
  assert.match(html, /Parcel rows remain quarantined/);
  assert.match(html, /LATEST SYNTHETIC RUN/);
  assert.match(html, /axiom-social-card\.png/);
  assert.doesNotMatch(html, /Your site is taking shape|react-loading-skeleton/);
});

test("keeps the production shell free of starter preview assets", async () => {
  const [page, layout, packageJson] = await Promise.all([
    readFile(new URL("../app/page.tsx", import.meta.url), "utf8"),
    readFile(new URL("../app/layout.tsx", import.meta.url), "utf8"),
    readFile(new URL("../package.json", import.meta.url), "utf8"),
  ]);

  assert.match(page, /function CoreOrb\(\)/);
  assert.match(page, /prefers-reduced-motion|GateTrack/);
  assert.match(layout, /AXIOM — California Property Intelligence/);
  assert.match(packageJson, /"name": "axiom-property-intelligence"/);
  assert.doesNotMatch(packageJson, /react-loading-skeleton/);

  await access(new URL("../public/axiom-social-card.png", import.meta.url));
  assert.deepEqual(
    await readdir(new URL("../app/_sites-preview", import.meta.url)),
    [],
  );
});
