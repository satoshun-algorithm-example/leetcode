CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N-1;
    RETURN (
        SELECT(
            SELECT distinct Salary FROM Employee
             ORDER BY Salary DESC
             LIMIT 1 OFFSET N
        ) as Salary
    );
END
