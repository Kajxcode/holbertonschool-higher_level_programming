-- script that lists all records by constraints
SELECT * FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;