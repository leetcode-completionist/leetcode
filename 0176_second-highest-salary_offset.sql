# Query for a distinct list of salaries in descending order
# limit the results to 1 with an offset of 1 from the start
# of the result. This will give us the salary immediately
# after the first result.
#
# Finally, we wrap the query with Ifnull so we can format
# the answer to be accepted.
SELECT Ifnull((SELECT DISTINCT salary
               FROM   employee
               ORDER  BY salary DESC
               LIMIT  1 offset 1), NULL) AS SecondHighestSalary 
