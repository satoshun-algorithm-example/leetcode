SELECT e1.Name as Employee FROM Employee as e1
 JOIN Employee as e2 ON e1.ManagerId = e2.Id
 WHERE e2.Salary < e1.Salary;