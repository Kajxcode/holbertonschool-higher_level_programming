-- script that imports database and lists ids
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id IN (
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    WHERE tv_show_genres.show_id = (
        SELECT id from tv_shows WHERE title = 'Dexter' LIMIT 1
    )
)
ORDER BY tv_genres.name ASC;