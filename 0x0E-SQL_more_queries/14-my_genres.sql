-- script that lists all shows contained in hbtn_0d_tvshows.
SELECT tg.name AS name
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
LEFT JOIN tv_shows AS ts ON tsg.show_id = ts.id
WHERE ts.title = "Dexter"
ORDER BY name ASC;
