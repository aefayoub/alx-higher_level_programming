-- script that lists all shows contained in hbtn_0d_tvshows.
SELECT ts.title AS title, tsg.genre_id AS genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
WHERE tsg.genre_id is NULL
ORDER BY title, genre_id ASC;
