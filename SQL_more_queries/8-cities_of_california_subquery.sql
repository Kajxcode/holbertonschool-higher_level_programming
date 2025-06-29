-- script that lists cities of california
SELECT id, name
FROM cities
WHERE cities_id = (
    SELECT id FROM states WHERE name = 'California' LIMIT 1
)
ORDER BY id ASC;