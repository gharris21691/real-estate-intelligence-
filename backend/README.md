# Backend

The Phase 1 backend is a standard-library Python foundation. It contains no downloader, scraper, live-source connector, or County-specific parser.

## Included

- external data-root configuration with repository-boundary checks;
- metadata-only SHA-256 source manifests;
- a field-level privacy policy;
- provisional canonical-record validation;
- synthetic-only normalization, exception routing, and reconciliation reports;
- machine-enforced source approval gates;
- an idempotent SQLite metadata/provenance schema; and
- local commands for configuration checks, database setup, and manifest output.

## Local setup

Python 3.11 or later is required. The tests can run without installing the package:

```bash
PYTHONPATH=backend python3 -m unittest discover -s tests -v
```

For an editable installation in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e .
```

Copy `.env.example` to an untracked `.env` or export the values in the shell. The current external data root is expected to be:

```text
/Volumes/GSTUDIOT7/Realestate_Projects/CA_Distressed_AI/real-estate-intelligence
```

The application does not load `.env` automatically. This avoids silently importing configuration; export the variables through the shell or a future approved secret/configuration tool.

## Safety boundary

`rei manifest` reads a source file only to calculate its size and SHA-256 digest. Its JSON output stores only the filename, never the full external path. Do not redirect manifest output into Git until it has been reviewed for non-sensitive metadata.

Run the end-to-end synthetic acceptance path from the repository root:

```bash
PYTHONPATH=backend python3 -m rei.cli validate-synthetic \
  data/fixtures/sacramento_assessment_synthetic.json
```

The command refuses files outside `data/fixtures` and refuses JSON that does not carry the exact synthetic-data notice. It reports a deterministic input fingerprint, transformation version, accepted/review/rejected counts, and non-sensitive issue codes. It does not write normalized records.

Inspect the current execution gates:

```bash
PYTHONPATH=backend python3 -m rei.cli source-status
```

The policy file is `config/source-policies.json`. Only the synthetic fixture is executable. The real Sacramento secured roll and GIS source have empty allowlists and remain disabled until every named approval gate is complete and their status is explicitly changed to `approved_for_pilot`.
