class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            next_row = []
            for i in range(len(res) + 1):
                if i == 0:
                    next_row.append(1)
                elif i == len(res):
                    next_row.append(1)
                else:
                    next_row.append(res[i-1] + res[i])
            res = next_row

        return res
