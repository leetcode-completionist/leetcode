# https://leetcode.com/problems/find-k-closest-elements/
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        
        right = bisect.bisect_left(arr, x)
        left = right - 1
        
        while right - left - 1 < k:
            if left == -1:
                right += 1
            elif right == n:
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        return arr[left + 1:right]
