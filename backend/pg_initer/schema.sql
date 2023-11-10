CREATE EXTENSION IF NOT EXISTS postgis;
CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.nodes (
    id UUID PRIMARY KEY,
    osm_id BIGINT,
    title TEXT,
    location geometry(POINT, 4326),
    role TEXT,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.railway_nodes (
    id UUID PRIMARY KEY,
    node_osm_id BIGINT,
    railway_osm_id BIGINT,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.railways (
    id UUID PRIMARY KEY,
    osm_id BIGINT,
    title TEXT,
    geo geometry(MULTILINESTRING, 4326),
    title_from TEXT,
    title_to TEXT,
    operator TEXT,
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

CREATE TABLE IF NOT EXISTS content.waybills (
    id UUID PRIMARY KEY,
    number TEXT,
    start_node_id UUID,
    finish_node_id UUID,
    geo geometry(MULTILINESTRING, 4326),
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE IF NOT EXISTS content.train_railways (
    id UUID PRIMARY KEY,
    train_id UUID,
    railway_id UUID,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);