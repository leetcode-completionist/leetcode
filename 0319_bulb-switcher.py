# https://leetcode.com/problems/bulb-switcher/
class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
            1st : 1
            2nd : 1 0
            3rd : 1 0 0
            4th : 1 0 0 1
            5th : 1 0 0 1 0
            6th : 1 0 0 1 0 0
            7th : 1 0 0 1 0 0 0
            8th : 1 0 0 1 0 0 0 0
            9th : 1 0 0 1 0 0 0 0 1

            Pattern: i bulbs are on at the i^2 rounds

            So n bulbs are on at n^(1/2) rounds
        """
        return int(n**(1/2))
