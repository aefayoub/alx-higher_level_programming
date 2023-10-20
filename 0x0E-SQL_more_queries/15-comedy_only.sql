-- script that lists all shows contained in hbtn_0d_tvshows.
SELECT ts.title AS title
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE tg.name = "Comedy"
ORDER BY title ASC;
