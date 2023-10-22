-- script that lists all shows contained in hbtn_0d_tvshowsi
SELECT tvg.name AS name
FROM tv_genres AS tvg
LEFT JOIN 
(
	SELECT tg.id, tg.name FROM tv_genres AS tg
       	JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
	JOIN tv_shows AS ts ON tsg.show_id = ts.id
	WHERE ts.title = "Dexter"
) g_dexter ON g_dexter.id = tvg.id
WHERE g_dexter.id IS NULL
ORDER BY name ASC;
