# Tests

The Phase 1 test suite covers external-path safety, metadata manifests, privacy policy enforcement, source approval gates, canonical validation, synthetic reconciliation, durable audit history, exception routing, and idempotent database initialization.

Run it from the repository root:

```bash
PYTHONPATH=backend python3 -m unittest discover -s tests -v
```

All fixtures are synthetic. Tests must never depend on the mounted external drive or real County records.
