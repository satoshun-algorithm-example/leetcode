SELECT Name as Employee FROM Employee as e1
 WHERE EXISTS(
    SELECT * FROM Employee as e2
        WHERE
            e2.Id = e1.ManagerId AND
            e2.Salary < e1.Salary
    );