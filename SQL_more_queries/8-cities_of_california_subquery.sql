-- script that lists cities of california
SELECT cities.id, cities name
FROM cities
WHERE cities.state.id = (
    SELECT id FROM states WHERE name = 'California' LIMIT 1
)
ORDER BY cities.id ASC;