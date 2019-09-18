SELECT Name as Customers FROM Customers as c
 WHERE NOT EXISTS(SELECT * FROM Orders as o
    WHERE c.id = o.CustomerId
 );
