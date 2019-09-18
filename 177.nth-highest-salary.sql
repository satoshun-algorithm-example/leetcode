CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N-1;
    RETURN (
        SELECT distinct Salary FROM Employee
            ORDER BY Salary DESC
            LIMIT N, 1
    );
END
