# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        [5,5,2,6,1]
         0,1,2,3,4

        1. Sort the numbers and collect indices.
           Runtime is O(nlog(n))

                   Reuse answer if same as prev
                   v
            [1,2,5,5,6]
             4,2,0,1,3

        2. Create a sorted list that lets us answer
           the question "How many indices came
           after the current index?"

            [1,2,5,5,6]
             4,2,0,1,3
             ^
            [4] - 0 indices came after '4'

               ^
              [2,4] - 1 index came after '2'

                 ^
                [0,2,4] - 2 indices came after '0'
                    
                   ^
                  [0,1,2,4] - 2 indices came after '1'

                     ^
                    [0,1,2,3,4] - 1 index came after '3'


            We will have the following by the end of this
            step. Runtime is O(nlog(n)).

               [1,2,5,5,6]
                4,2,0,1,3
               [0,1,2,2,1]

         3. Finally, we will sort the results from previous step
            by its corresponding index. For example:

                0,1,2,3,4
               [2,2,1,1,0]

            This gives us our final answer. Runtime remains O(nlog(n))
        """
        # 1. Collect num with index in increasing order.
        num_with_index = []
        for i, num in enumerate(nums):
            num_with_index.append((num, i))
        num_with_index.sort()

        # 2. Iterate through num_with_index and determine
        #    count of smaller numbers after self.
        seen_indices = SortedList()
        index_with_count = []

        for num, i in num_with_index:
            # Use binary search to determine how many smaller
            # numbers we have seen so far.
            n = len(seen_indices)
            j = seen_indices.bisect_left(i)
            index_with_count.append((i, n - j))
            
            # Add index seen in sorted order.
            seen_indices.add(i)

        # 3. Sort index_with_count by index and return the count
        return [e[1] for e in sorted(index_with_count)]
