SELECT
    s.Score,
    (SELECT COUNT(*) FROM (SELECT distinct Score FROM Scores) tmp WHERE s.Score <= Score) as Rank
    FROM Scores as s
    ORDER BY s.Score DESC;
