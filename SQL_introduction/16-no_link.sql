-- script that lists all records by constraints
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;