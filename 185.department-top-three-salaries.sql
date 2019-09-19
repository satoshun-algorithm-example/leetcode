SELECT d.Name as Department, e.Name as Employee, e.Salary as Salary
 FROM Employee as e
 INNER JOIN Department as d ON d.Id = e.DepartmentId
 WHERE 3 > (
    SELECT COUNT(DISTINCT Salary) FROM Employee
    WHERE
        DepartmentId = e.DepartmentId AND
        Salary > e.Salary
 )
 ORDER BY d.Name, e.Salary DESC;
