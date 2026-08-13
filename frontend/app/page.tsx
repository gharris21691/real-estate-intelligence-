"use client";

import { useEffect, useState } from "react";

const sources = [
  {
    code: "SAC-01",
    name: "Secured assessment roll",
    agency: "Sacramento County Assessor",
    status: "COMPLIANCE HOLD",
    state: "hold",
    gates: 1,
  },
  {
    code: "SAC-02",
    name: "Active parcel base",
    agency: "Sacramento County GIS",
    status: "ACCESS PENDING",
    state: "pending",
    gates: 0,
  },
  {
    code: "SYN-00",
    name: "Synthetic assessment fixture",
    agency: "Internal test environment",
    status: "EXECUTABLE",
    state: "live",
    gates: 5,
  },
];

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

function GateTrack({ complete }: { complete: number }) {
  return (
    <div className="gate-track" aria-label={`${complete} of 5 approval gates complete`}>
      {gateLabels.map((gate, index) => (
        <span className={index < complete ? "gate gate--on" : "gate"} key={gate}>
          <i />
          {gate}
        </span>
      ))}
    </div>
  );
}

export default function Home() {
  const [view, setView] = useState<"overview" | "sources">("overview");

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
          <button className={view === "sources" ? "nav-active" : ""} onClick={() => setView("sources")}>Sources</button>
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
          <strong>03</strong>
          <small>1 executable / 2 held</small>
        </article>
        <article>
          <span className="metric-label">LATEST RUN</span>
          <strong>02</strong>
          <small>observations accepted</small>
        </article>
        <article>
          <span className="metric-label">RECONCILIATION</span>
          <strong>100<span>%</span></strong>
          <small>zero unresolved issues</small>
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
            <article className="source-row" key={source.code}>
              <span className="source-index">0{index + 1}</span>
              <div className="source-identity">
                <span>{source.code}</span>
                <h3>{source.name}</h3>
                <p>{source.agency}</p>
              </div>
              <GateTrack complete={source.gates} />
              <span className={`source-status source-status--${source.state}`}><i />{source.status}</span>
              <button aria-label={`View ${source.name} details`}>↗</button>
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
            <div><strong>2</strong><span>ACCEPTED</span></div>
          </div>
          <div className="run-stats">
            <div><span>REVIEW</span><strong>0</strong></div>
            <div><span>REJECTED</span><strong>0</strong></div>
            <div><span>ISSUES</span><strong>0</strong></div>
          </div>
          <div className="fingerprint">
            <span>INPUT FINGERPRINT</span>
            <code>5824810d…bea822a1</code>
          </div>
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
    </main>
  );
}
