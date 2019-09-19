SELECT d.Name as Department, e.Name as Employee, e.Salary as Salary
 FROM Employee as e
 INNER JOIN Department as d ON d.Id = e.DepartmentId
 WHERE e.Salary IN (
    SELECT Salary FROM Employee
    WHERE DepartmentId = e.DepartmentId
    ORDER BY Salary DESC
    LIMIT 3
);
