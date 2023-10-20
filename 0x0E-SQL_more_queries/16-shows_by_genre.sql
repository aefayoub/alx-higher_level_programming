-- script that lists all shows contained in hbtn_0d_tvshows.
SELECT ts.title AS title, tg.name AS name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres AS tg ON tsg.genre_id = tg.id
ORDER BY title, name ASC;
