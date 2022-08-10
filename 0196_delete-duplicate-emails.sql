# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE FROM Person
WHERE id NOT IN (
    # we need to nest it because
    # leetcode's MySQL env doesn't
    # allow deletions on the same
    # table in the select statement
    #
    # however wrapping it as a
    # subquery works
    SELECT *
    FROM (
        SELECT MIN(id)
        FROM Person
        GROUP BY email
    ) p
)
