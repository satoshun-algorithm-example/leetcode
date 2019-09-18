SELECT w1.ID as Id FROM Weather as w1
 WHERE w1.Temperature > (
    SELECT w2.Temperature FROM Weather as w2
        WHERE subdate(w1.RecordDate, 1) = w2.RecordDate
 );
