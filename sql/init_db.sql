CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY,
    url TEXT NOT NULL,
    token TEXT,
    create_ts TIMESTAMP,
    update_ts TIMESTAMP
)