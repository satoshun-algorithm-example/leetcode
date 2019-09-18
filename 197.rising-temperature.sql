SELECT w1.ID as Id FROM Weather as w1
 WHERE w1.Temperature > (
    SELECT w2.Temperature FROM Weather as w2
        WHERE TO_DAYS(w1.RecordDate) - TO_DAYS(w2.RecordDate) = 1
 );
