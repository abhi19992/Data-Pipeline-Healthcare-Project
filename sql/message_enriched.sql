-- =====================================================
-- Create the message_enriched table by joining messages and statuses tables
-- with pivoted status timestamps for easier analysis.
-- The table includes all columns from messages and additional timestamp columns
-- for each status type from statuses.
-- =====================================================
CREATE TABLE IF NOT EXISTS message_enriched AS
WITH status_pivot AS (
    SELECT
        s.message_uuid,
        MAX(CASE WHEN s.status = 'sent' THEN s.timestamp END) AS sent_timestamp,
        MAX(CASE WHEN s.status = 'delivered' THEN s.timestamp END) AS delivered_timestamp,
        MAX(CASE WHEN s.status = 'read' THEN s.timestamp END) AS read_timestamp,
        MAX(CASE WHEN s.status = 'failed' THEN s.timestamp END) AS failed_timestamp,
        MAX(CASE WHEN s.status = 'deleted' THEN s.timestamp END) AS deleted_timestamp
    FROM statuses s
    GROUP BY s.message_uuid
)
SELECT 
    m.id,
    m.message_type,
    m.masked_addressees,
    m.masked_author,
    m.content,
    m.author_type,
    m.direction,
    m.external_id,
    m.external_timestamp,
    m.masked_from_addr,
    m.is_deleted,
    m.last_status,
    m.last_status_timestamp,
    m.rendered_content,
    m.source_type,
    m.uuid,
    m.inserted_at AS message_inserted_at,
    m.updated_at AS message_updated_at,
    sp.sent_timestamp,
    sp.delivered_timestamp,
    sp.read_timestamp,
    sp.failed_timestamp,
    sp.deleted_timestamp
FROM messages m
LEFT JOIN status_pivot sp
    ON m.uuid = sp.message_uuid;
