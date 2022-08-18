# https://leetcode.com/problems/trips-and-users/
#
# Write your MySQL query statement below
SELECT request_at AS "Day",
       Round(Count(IF(status LIKE 'cancelled%', 1, NULL)) / Count(*), 2) AS "Cancellation Rate"
FROM   trips
WHERE  client_id NOT IN (SELECT users_id
                         FROM   users
                         WHERE  banned = 'Yes'
                                AND role = 'client')
       AND driver_id NOT IN (SELECT users_id
                             FROM   users
                             WHERE  banned = 'Yes'
                                    AND role = 'driver')
       AND request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP  BY request_at 
