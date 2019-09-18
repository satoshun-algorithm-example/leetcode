SELECT(
    SELECT distinct Salary FROM Employee
     ORDER BY Salary DESC LIMIT 1 OFFSET 1
) as SecondHighestSalary;
