# Write your MySQL query statement below
SELECT p.FirstName, p.LastName, a.City, a.State
 FROM Person as p
  LEFT JOIN Address as a
   ON a.PersonId = p.PersonId;