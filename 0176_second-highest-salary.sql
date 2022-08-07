# Find the second highest salary
#
# 1. first find the highest salary
# 2. then find the next highest salary
#
SELECT Max(salary) AS "SecondHighestSalary"
FROM   employee
WHERE  salary < (SELECT Max(salary)
                 FROM   employee) 
