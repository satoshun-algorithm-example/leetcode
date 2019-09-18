SELECT distinct l1.Num as ConsecutiveNums FROM Logs as l1
 INNER JOIN Logs as l2 ON l1.Id = (l2.Id + 1)
 INNER JOIN Logs as l3 ON l2.Id = (l3.Id + 1)
 WHERE l1.Num = l2.Num AND l2.Num = l3.Num;
