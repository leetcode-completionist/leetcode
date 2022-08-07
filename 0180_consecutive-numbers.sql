# Write your MySQL query statement below
SELECT
    DISTINCT l1.num as ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    # has id - 1
    l1.id = l2.id - 1
    # has id - 2
    AND l1.id = l3.id - 2
    # for the same number
    AND l1.num = l2.num
    AND l2.num = l3.num
