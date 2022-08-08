# Write your MySQL query statement below
SELECT
    d.name as "Department",
    e.name as "Employee",
    e.salary as "Salary"
FROM
    Employee e
    INNER JOIN Department d
    ON e.departmentId = d.id
    INNER JOIN (
        SELECT departmentId, MAX(salary) as max_salary
        FROM Employee
        GROUP BY departmentId
    ) department_max_salaries
    ON e.departmentId = department_max_salaries.departmentId
WHERE
    e.salary = department_max_salaries.max_salary
