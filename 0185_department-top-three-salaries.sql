# Write your MySQL query statement below
SELECT DISTINCT
    d.name as "Department",
    e.name as "Employee",
    e.salary as "Salary"
FROM
    Employee e
    INNER JOIN Department d
    ON e.departmentId = d.id
    INNER JOIN (
        SELECT
            departmentId,
            salary,
            DENSE_RANK() OVER (
                PARTITION BY departmentId
                ORDER BY salary DESC
            ) AS "rank"
        FROM
            Employee
    ) ranked_salaries
    ON e.departmentId = ranked_salaries.departmentId
    AND e.salary = ranked_salaries.salary
WHERE
    ranked_salaries.rank < 4
