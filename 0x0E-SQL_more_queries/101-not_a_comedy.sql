-- script that lists all shows contained in hbtn_0d_tvshowsi
SELECT tvs.title AS title
FROM tv_shows AS tvs
LEFT JOIN 
(
	SELECT ts.id, ts.title FROM tv_shows AS ts
       	JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
	JOIN tv_genres AS tg ON tsg.genre_id = tg.id
	WHERE tg.name = "Comedy"
) s_comedy ON s_comedy.id = tvs.id
WHERE s_comedy.id IS NULL
ORDER BY title ASC;
