-- database dump from hbtn_0d_tvshows_rate to your MySQL server.
SELECT tg.name AS name, SUM(tsr.rate) AS rating
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
INNER JOIN tv_shows AS ts ON tsg.show_id = ts.id
INNER JOIN tv_show_ratings AS tsr ON ts.id = tsr.show_id 
GROUP BY name
ORDER BY rating DESC
