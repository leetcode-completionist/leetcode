# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = math.inf
        max_salary = 0
        total_salary = 0
        
        for s in salary:
            total_salary += s
            min_salary = min(min_salary, s)
            max_salary = max(max_salary, s)
            
        return ((total_salary - min_salary - max_salary) /
                (len(salary) - 2))
