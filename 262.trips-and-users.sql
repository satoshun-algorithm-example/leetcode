SELECT t.Request_at as Day,
 AVG(CASE WHEN u.Role = "client" AND t.Status = "cancelled_by_client" AND u.Banned = "Yes" THEN 0
          WHEN u.Role = "driver" AND t.Status = "cancelled_by_driver" AND u.Banned = "Yes" THEN 0
          ELSE 1 END
 ) as "Cancellation Rate"
 FROM Trips as t
 INNER JOIN Users as u ON u.Users_Id = t.Client_Id OR u.Users_Id = t.Driver_Id
 GROUP BY Request_at;
