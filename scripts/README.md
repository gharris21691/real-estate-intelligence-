# Scripts

`export_frontend_snapshot.py` creates the public, synthetic-only JSON snapshot
consumed by the AXIOM control room. Run it from the repository root with
`PYTHONPATH=backend python3 scripts/export_frontend_snapshot.py` after a source
policy or synthetic fixture changes. The export contains public gate status and
quality counts only; it excludes raw parcel records and field names.

`index_sacramento_reference_batch.py` inventories the Assessor land-use PDF and
Excel quick reference on the external data drive. It publishes only filenames,
checksums, structural metadata, and general code families to the frontend; the
source documents remain on the external drive.

Reserved for future operational tooling. Source-research work must not add acquisition scripts.
