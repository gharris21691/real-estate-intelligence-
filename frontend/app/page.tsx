"use client";

import { useEffect, useState } from "react";
import dashboardData from "@/data/control-room.json";

type GateName = "access" | "terms" | "privacy" | "data" | "operations";
type Source = (typeof dashboardData.sources)[number];

const sources = dashboardData.sources;
const latestRun = dashboardData.latest_run;
const sourceCodes: Record<string, string> = {
  ca_sacramento_assessor_secured_roll: "SAC-01",
  ca_sacramento_gis_active_parcel_base: "SAC-02",
  synthetic_sacramento_assessment_fixture: "SYN-00",
};
const sourceAgencies: Record<string, string> = {
  ca_sacramento_assessor_secured_roll: "Sacramento County Assessor",
  ca_sacramento_gis_active_parcel_base: "Sacramento County GIS",
  synthetic_sacramento_assessment_fixture: "Internal test environment",
};

const gateLabels = ["ACCESS", "TERMS", "PRIVACY", "DATA", "OPS"];

function SystemClock() {
  const [time, setTime] = useState("--:--:--");

  useEffect(() => {
    const tick = () =>
      setTime(
        new Intl.DateTimeFormat("en-US", {
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
          hour12: false,
          timeZone: "America/Los_Angeles",
        }).format(new Date()),
      );
    tick();
    const timer = window.setInterval(tick, 1000);
    return () => window.clearInterval(timer);
  }, []);

  return <span>{time} PST</span>;
}

function CoreOrb() {
  return (
    <div className="core-wrap" aria-label="Synthetic intelligence core online">
      <div className="core-coordinates core-coordinates--top">38.5816° N</div>
      <div className="core-coordinates core-coordinates--bottom">121.4944° W</div>
      <div className="orbit orbit--outer">
        <span className="orbit-node orbit-node--one" />
        <span className="orbit-node orbit-node--two" />
      </div>
      <div className="orbit orbit--mid" />
      <div className="orbit orbit--inner" />
      <div className="core-scan" />
      <div className="core-center">
        <span className="core-kicker">CORE</span>
        <strong>ONLINE</strong>
        <span className="core-value">100%</span>
      </div>
      <div className="core-tick core-tick--a" />
      <div className="core-tick core-tick--b" />
      <div className="core-tick core-tick--c" />
    </div>
  );
}

function sourceState(source: Source) {
  if (source.executable) return { label: "EXECUTABLE", state: "live" };
  if (source.approval_status.includes("hold")) return { label: "COMPLIANCE HOLD", state: "hold" };
  return { label: "ACCESS PENDING", state: "pending" };
}

function GateTrack({ source }: { source: Source }) {
  return (
    <div className="gate-track" aria-label={`${Object.values(source.gates).filter(Boolean).length} of 5 approval gates complete`}>
      {gateLabels.map((gate) => (
        <span className={source.gates[gate.toLowerCase() as GateName] ? "gate gate--on" : "gate"} key={gate}>
          <i />
          {gate}
        </span>
      ))}
    </div>
  );
}

export default function Home() {
  const [view, setView] = useState<"overview" | "sources">("overview");
  const [selectedSource, setSelectedSource] = useState<Source | null>(null);
  const [verified, setVerified] = useState(false);

  const executableCount = sources.filter((source) => source.executable).length;

  const verifySnapshot = () => {
    setVerified(true);
    window.setTimeout(() => setVerified(false), 3200);
  };

  return (
    <main>
      <div className="ambient-grid" />
      <div className="scanline" />

      <header className="topbar">
        <a className="brand" href="#top" aria-label="Axiom home">
          <span className="brand-mark"><i /><i /><i /></span>
          <span>
            <strong>AXIOM</strong>
            <small>PROPERTY INTELLIGENCE</small>
          </span>
        </a>
        <nav aria-label="Primary navigation">
          <button className={view === "overview" ? "nav-active" : ""} onClick={() => setView("overview")}>Overview</button>
          <button className={view === "sources" ? "nav-active" : ""} onClick={() => { setView("sources"); document.querySelector("#sources")?.scrollIntoView(); }}>Sources</button>
          <a href="#audit">Audit</a>
        </nav>
        <div className="system-meta">
          <span><i className="status-dot" /> SYSTEM STABLE</span>
          <SystemClock />
        </div>
      </header>

      <section className="hero" id="top">
        <div className="hero-copy">
          <div className="eyebrow"><span>01 / 04</span> CALIFORNIA PROPERTY INTELLIGENCE</div>
          <h1>Order the<br /><em>signal.</em></h1>
          <p>
            A source-grounded intelligence layer for California property research—built to expose provenance, uncertainty, and every approval gate.
          </p>
          <div className="hero-actions">
            <a className="primary-action" href="#sources">Enter system <span>↗</span></a>
            <span className="environment"><i /> SYNTHETIC ENVIRONMENT</span>
          </div>
        </div>
        <div className="hero-core">
          <CoreOrb />
          <div className="core-caption">
            <span>NODE / SACRAMENTO</span>
            <span>MODE / READ ONLY</span>
          </div>
        </div>
        <div className="hero-rail">
          <span className="rail-number">001</span>
          <div className="rail-line"><i /></div>
          <span>PROVENANCE FIRST</span>
          <span>NO LIVE RECORDS</span>
        </div>
      </section>

      <section className="metrics" id="audit">
        <div className="section-index">02 / SYSTEM STATE</div>
        <article>
          <span className="metric-label">SOURCE POLICIES</span>
          <strong>{String(sources.length).padStart(2, "0")}</strong>
          <small>{executableCount} executable / {sources.length - executableCount} held</small>
        </article>
        <article>
          <span className="metric-label">LATEST RUN</span>
          <strong>{String(latestRun.input_count).padStart(2, "0")}</strong>
          <small>observations accepted</small>
        </article>
        <article>
          <span className="metric-label">RECONCILIATION</span>
          <strong>{latestRun.reconciliation_passed ? "100" : "0"}<span>%</span></strong>
          <small>{Object.keys(latestRun.issue_counts).length} unresolved issues</small>
        </article>
        <article className="metric-visual">
          <div className="signal-bars" aria-hidden="true">
            {[38, 55, 42, 72, 64, 89, 58, 78, 100, 83, 92, 74].map((height, index) => (
              <i key={index} style={{ height: `${height}%` }} />
            ))}
          </div>
          <small>INTEGRITY SIGNAL / NOMINAL</small>
        </article>
      </section>

      <section className="sources-section" id="sources">
        <div className="sources-heading">
          <div>
            <div className="eyebrow"><span>03 / 04</span> SOURCE CONTROL</div>
            <h2>{view === "overview" ? "Trust before" : "Source"}<br /><em>{view === "overview" ? "velocity." : "matrix."}</em></h2>
          </div>
          <p>
            Every live source stays dark until access, terms, privacy, data quality, and operations gates are explicitly cleared.
          </p>
        </div>

        <div className="source-list">
          {sources.map((source, index) => (
            <article className="source-row" key={source.id}>
              <span className="source-index">0{index + 1}</span>
              <div className="source-identity">
                <span>{sourceCodes[source.id]}</span>
                <h3>{source.source_name}</h3>
                <p>{sourceAgencies[source.id]}</p>
              </div>
              <GateTrack source={source} />
              <span className={`source-status source-status--${sourceState(source).state}`}><i />{sourceState(source).label}</span>
              <button onClick={() => setSelectedSource(source)} aria-label={`View ${source.source_name} details`}>↗</button>
            </article>
          ))}
        </div>
      </section>

      <section className="run-section">
        <div className="run-copy">
          <div className="eyebrow"><span>04 / 04</span> LATEST SYNTHETIC RUN</div>
          <h2>Evidence,<br /><em>intact.</em></h2>
          <p>One immutable fixture. Two normalized observations. Every transformation accounted for.</p>
        </div>
        <div className="run-panel">
          <div className="run-panel-head">
            <span>RUN / SACRAMENTO-SYNTHETIC-V1</span>
            <span className="run-live"><i /> COMPLETE</span>
          </div>
          <div className="run-ring">
            <div><strong>{latestRun.accepted_count}</strong><span>ACCEPTED</span></div>
          </div>
          <div className="run-stats">
            <div><span>REVIEW</span><strong>{latestRun.review_count}</strong></div>
            <div><span>REJECTED</span><strong>{latestRun.rejected_count}</strong></div>
            <div><span>ISSUES</span><strong>{Object.keys(latestRun.issue_counts).length}</strong></div>
          </div>
          <div className="fingerprint">
            <span>INPUT FINGERPRINT</span>
            <code>{latestRun.input_sha256.slice(0, 8)}…{latestRun.input_sha256.slice(-8)}</code>
          </div>
          <button className={`verify-action ${verified ? "verify-action--done" : ""}`} onClick={verifySnapshot}>
            <span>{verified ? "SNAPSHOT VERIFIED" : "VERIFY SNAPSHOT"}</span>
            <i>{verified ? "✓" : "↗"}</i>
          </button>
        </div>
      </section>

      <footer>
        <div className="brand footer-brand">
          <span className="brand-mark"><i /><i /><i /></span>
          <span><strong>AXIOM</strong><small>PROPERTY INTELLIGENCE</small></span>
        </div>
        <p>Synthetic interface / no live county records</p>
        <span>BUILD 00.01.00</span>
      </footer>

      {selectedSource && (
        <div className="source-modal" role="dialog" aria-modal="true" aria-labelledby="source-detail-title">
          <section className="source-drawer">
            <div className="drawer-head">
              <span>{sourceCodes[selectedSource.id]} / SOURCE DETAIL</span>
              <button onClick={() => setSelectedSource(null)} aria-label="Close source details">CLOSE ×</button>
            </div>
            <div className="drawer-orb"><i /></div>
            <p className="drawer-kicker">{selectedSource.county.toUpperCase()} / {selectedSource.data_class.toUpperCase()}</p>
            <h2 id="source-detail-title">{selectedSource.source_name}</h2>
            <div className="drawer-status">
              <span className={`source-status source-status--${sourceState(selectedSource).state}`}><i />{sourceState(selectedSource).label}</span>
              <span>{selectedSource.allowed_field_count} ALLOWED FIELDS</span>
              <span>{selectedSource.prohibited_field_count} PROTECTED FIELDS</span>
            </div>
            <div className="drawer-gates">
              {gateLabels.map((label) => {
                const active = selectedSource.gates[label.toLowerCase() as GateName];
                return <div className={active ? "drawer-gate drawer-gate--on" : "drawer-gate"} key={label}><i />{label}<span>{active ? "CLEARED" : "PENDING"}</span></div>;
              })}
            </div>
            <div className="drawer-blockers">
              <span>DECISION LOG</span>
              {selectedSource.hold_reasons.length ? (
                <ol>{selectedSource.hold_reasons.map((reason) => <li key={reason}>{reason}</li>)}</ol>
              ) : (
                <p>All synthetic execution gates are cleared. This does not authorize live County data.</p>
              )}
            </div>
            <p className="drawer-footnote">Repository snapshot / {new Date(dashboardData.generated_at).toLocaleString("en-US", { timeZone: "America/Los_Angeles" })} PST</p>
          </section>
        </div>
      )}
    </main>
  );
}
