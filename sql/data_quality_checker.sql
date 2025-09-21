##DATA QUALITY CHECKER QUERIES

-- =====================================================
-- Duplicate messages: same content and same inserted_at
-- =====================================================
SELECT
    CASE
        WHEN LOWER(direction) = 'inbound' THEN content
        WHEN LOWER(direction) = 'outbound' THEN rendered_content
        ELSE NULL
    END AS message_content,
    message_inserted_at,
    COUNT(*) AS duplicate_count,
    STRING_AGG(CAST(uuid AS text), ', ' ORDER BY uuid) AS duplicate_uuids
FROM message_enriched
GROUP BY message_content, message_inserted_at
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;

-- =====================================================
-- Duplicate UUID:: 2 records 
-- =====================================================
SELECT
    uuid,
    CASE
        WHEN LOWER(direction) = 'inbound' THEN content
        WHEN LOWER(direction) = 'outbound' THEN rendered_content
        ELSE NULL
    END AS message_content,
    message_inserted_at,
    COUNT(*) AS duplicate_count
FROM message_enriched
GROUP BY uuid,message_content, message_inserted_at
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;


-- =====================================================
-- Check for NULL UUID(P.K) -- 
-- =====================================================
SELECT
    COUNT(*)
FROM
    message_enriched
WHERE
    uuid IS NULL;


-- =====================================================
-- Missing content: inbound messages with NULL content,
-- or outbound messages with NULL rendered_content
-- =====================================================
SELECT *
FROM message_enriched
WHERE (LOWER(direction) = 'inbound' AND content IS NULL)
   OR (LOWER(direction) = 'outbound' AND rendered_content IS NULL)
ORDER BY message_inserted_at;



-- =====================================================
--  Check for deleted status 
-- =====================================================
SELECT *
FROM message_enriched;
WHERE is_deleted = "TRUE" ; 
last_status != 'deleted';


-- =====================================================
-- Find statuses that don't have a corresponding message
-- =====================================================
SELECT 
    s.message_uuid,
    COUNT(*) AS orphan_status_count
FROM statuses s
LEFT JOIN messages m
    ON s.message_uuid = m.uuid
WHERE m.uuid IS NULL
GROUP BY s.message_uuid;
