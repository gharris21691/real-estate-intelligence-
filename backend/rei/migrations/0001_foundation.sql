PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS schema_migration (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT OR IGNORE INTO schema_migration (version) VALUES (1);

CREATE TABLE IF NOT EXISTS source_definition (
    source_id TEXT PRIMARY KEY,
    jurisdiction TEXT NOT NULL,
    agency TEXT NOT NULL,
    source_name TEXT NOT NULL,
    approval_status TEXT NOT NULL CHECK (
        approval_status IN ('disabled', 'candidate', 'approved_for_pilot', 'blocked')
    ),
    allowed_fields_json TEXT NOT NULL DEFAULT '[]',
    prohibited_fields_json TEXT NOT NULL DEFAULT '[]',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS acquisition_run (
    run_id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL REFERENCES source_definition(source_id),
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('planned', 'running', 'succeeded', 'failed', 'cancelled')),
    transformation_version TEXT NOT NULL,
    accepted_count INTEGER NOT NULL DEFAULT 0 CHECK (accepted_count >= 0),
    rejected_count INTEGER NOT NULL DEFAULT 0 CHECK (rejected_count >= 0),
    review_count INTEGER NOT NULL DEFAULT 0 CHECK (review_count >= 0),
    error_summary TEXT
);

CREATE TABLE IF NOT EXISTS source_artifact (
    artifact_id TEXT PRIMARY KEY,
    run_id TEXT REFERENCES acquisition_run(run_id),
    source_id TEXT NOT NULL REFERENCES source_definition(source_id),
    file_name TEXT NOT NULL,
    external_uri TEXT NOT NULL,
    byte_size INTEGER NOT NULL CHECK (byte_size >= 0),
    sha256 TEXT NOT NULL CHECK (length(sha256) = 64),
    observed_at TEXT NOT NULL,
    effective_date TEXT,
    classification TEXT NOT NULL,
    UNIQUE (source_id, sha256)
);

CREATE TABLE IF NOT EXISTS parcel_observation (
    observation_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL REFERENCES acquisition_run(run_id),
    source_artifact_id TEXT NOT NULL REFERENCES source_artifact(artifact_id),
    jurisdiction_fips TEXT NOT NULL,
    source_apn TEXT NOT NULL,
    roll_year INTEGER NOT NULL,
    situs_address_raw TEXT,
    assessed_land_value TEXT,
    assessed_improvement_value TEXT,
    total_assessed_value TEXT,
    exemption_value TEXT,
    tax_rate_area_code TEXT,
    assessor_land_use_code TEXT,
    recorder_book_page TEXT,
    source_record_key TEXT NOT NULL,
    transformation_version TEXT NOT NULL,
    validation_status TEXT NOT NULL CHECK (validation_status IN ('accepted', 'review', 'rejected')),
    observed_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS parcel_observation_apn_year
    ON parcel_observation (jurisdiction_fips, source_apn, roll_year);

CREATE TABLE IF NOT EXISTS validation_issue (
    issue_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL REFERENCES acquisition_run(run_id),
    observation_id TEXT REFERENCES parcel_observation(observation_id),
    source_record_key TEXT NOT NULL,
    field_name TEXT,
    issue_code TEXT NOT NULL,
    non_sensitive_detail TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
