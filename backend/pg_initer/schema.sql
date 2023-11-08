CREATE EXTENSION IF NOT EXISTS postgis;
CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.nodes (
    id UUID PRIMARY KEY,
    osm_id TEXT,
    title TEXT,
    location geometry(POINT, 4326),
    role TEXT,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.railways (
    id UUID PRIMARY KEY,
    osm_id TEXT,
    title TEXT,
    geo geometry(MULTILINESTRING, 4326),
    title_from TEXT,
    title_to TEXT,
    network TEXT,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.wagons (
    id UUID PRIMARY KEY,
    train_id UUID,
    number INTEGER,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.trains (
    id UUID PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);