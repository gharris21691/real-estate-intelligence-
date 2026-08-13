# Scripts

`export_frontend_snapshot.py` creates the public, synthetic-only JSON snapshot
consumed by the AXIOM control room. Run it from the repository root with
`PYTHONPATH=backend python3 scripts/export_frontend_snapshot.py` after a source
policy or synthetic fixture changes. The export contains public gate status and
quality counts only; it excludes raw parcel records and field names.

Reserved for future operational tooling. Source-research work must not add acquisition scripts.
