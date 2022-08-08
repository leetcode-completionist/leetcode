# Write your MySQL query statement below
SELECT 
  name as "Employee" 
FROM 
  Employee e 
  INNER JOIN (
    SELECT 
      id, 
      salary 
    FROM 
      Employee 
    WHERE 
      id IN (
        SELECT 
          DISTINCT managerId 
        FROM 
          Employee 
        WHERE 
          managerId IS NOT NULL
      )
  ) m ON e.managerId = m.id 
WHERE 
  e.salary > m.salary
