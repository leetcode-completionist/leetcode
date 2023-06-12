class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        new_box = [['.'] * m for _ in range(n)]
        
        for i in range(m):
            bound = n
            cur = n - 1
            while cur >= 0:
                if box[i][cur] == "*":
                    new_box[cur][m - i - 1] = "*"
                    bound = cur
                elif box[i][cur] == "#":
                    new_box[bound - 1][m - i - 1] = "#"
                    bound -= 1                    
                cur -= 1
        
        return new_box
