SELECT
    s.Score,
    (SELECT COUNT(distinct Score) FROM Scores WHERE s.Score <= Score) as Rank
    FROM Scores as s
    ORDER BY s.Score DESC;
