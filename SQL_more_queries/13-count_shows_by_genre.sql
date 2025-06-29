-- script that imports database and lists ids
SELECT genre.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genre.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;