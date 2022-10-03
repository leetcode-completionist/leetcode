# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if not colors:
            return 0

        res = 0

        prev_color = colors[0]
        running_sum = neededTime[0]
        max_time = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] != prev_color:
                # remove all balloons in the previous group
                # except the balloon with the max neededTime
                res += running_sum - max_time

                # reset all var to current balloon
                prev_color = colors[i]
                running_sum = neededTime[i]
                max_time = neededTime[i]
            else:
                # same group as previous balloon
                running_sum += neededTime[i]
                max_time = max(max_time, neededTime[i])

        if (diff := running_sum - max_time) > 0:
            # handle last group
            res += diff
        
        return res
