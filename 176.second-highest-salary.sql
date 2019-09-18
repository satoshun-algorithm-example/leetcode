DELETE p1 FROM Person as p1
 INNER JOIN Person as p2 ON p1.Email = p2.Email
 WHERE p1.Id > p2.Id;
