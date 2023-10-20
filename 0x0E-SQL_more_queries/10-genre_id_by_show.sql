-- script that lists all shows contained in hbtn_0d_tvshows.
SELECT ts.title AS title, tvsg.genre_id AS genre_id
FROM tv_shows as ts
INNER JOIN tv_show_genres AS tvsg ON tvsg.show_id = ts.id
ORDER BY title, genre_id ASC;
