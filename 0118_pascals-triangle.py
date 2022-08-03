class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            last_row = res[-1]
            next_row = []
            for i in range(len(last_row) + 1):
                if i == 0:
                    next_row.append(1)
                elif i == len(last_row):
                    next_row.append(1)
                else:
                    next_row.append(last_row[i-1] + last_row[i])
            res.append(next_row)

        return res
