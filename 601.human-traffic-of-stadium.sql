SELECT distinct s1.id, s1.visit_date, s1.people FROM stadium as s1, stadium as s2, stadium as s3
 WHERE
     (
        (s1.id + 1 = s2.id AND s2.id + 1 = s3.id) OR
        (s1.id - 1 = s2.id AND s2.id - 1 = s3.id) OR
        (s1.id - 1 = s2.id AND s1.id + 1 = s3.id)
     ) AND s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100
     ORDER BY s1.id ASC;
