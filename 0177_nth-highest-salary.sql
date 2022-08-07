CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  # MySQL's offset can only take a variable, not an expressiong (i.e. n - 1)
  # As a result, we need to initialize a variable for offset.
  DECLARE salary_offset INT;
  SET salary_offset = N - 1;
  RETURN (
      # Retrieves the nth salary from a distinct list of salaries ordered in
      # descending order
      SELECT Ifnull((SELECT DISTINCT salary
                     FROM   employee
                     ORDER  BY salary DESC
                     LIMIT  1 offset salary_offset), NULL) AS SecondHighestSalary
  );
END
