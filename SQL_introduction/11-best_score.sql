-- script that lists all records with score >= 10
SELECT score, name
FROM second_table >= 10
ORDER BY score DESC;