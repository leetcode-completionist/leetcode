class NumArray:

    def __init__(self, nums: List[int]):
        """
        Building the segment tree:

        - allocate an array 2*len(nums)
        - copy nums into last half of the arr
        - starting from the rear: arr[i // 2] += arr[i]

            [0 , 22, 18, 4, 9, 9, 1, 3, 5, 4, 2, 7 ]
         i:  0   1   2   3  4  5  6  7  8  9  10 11
                                  ^
                                  |
                                  original array starts here
        """
        self.nums_length = len(nums)
        self.segment_tree = [0] * self.nums_length
        self.segment_tree.extend(nums)
        
        for i in range(len(self.segment_tree) - 1, 1, -1):
            self.segment_tree[i // 2] += self.segment_tree[i]
        

    def update(self, index: int, val: int) -> None:
        """
        Updating the segment tree:

        - determine the difference of val - arr[i]
        - change arr[i] to val
        - bubble up the difference and add to each parent

                                     change to 4 from 3
                                     diff of (4 - 1 = 1)
                                     |
                                     V
            [0,  23, 18, 5, 9, 9, 1, 4, 5, 4, 2, 7 ]
         i:  0   1   2   3  4  5  6  7  8  9  10 11
                 ^      ^
                 |      |
                 |      add diff (4 + 1)
                 |
                 add diff (22 + 1)
        """
        index += self.nums_length
        diff = val - self.segment_tree[index]
        self.segment_tree[index] = val
        while index > 1:
            self.segment_tree[index // 2] += diff
            index = index // 2


    def sumRange(self, left: int, right: int) -> int:
        """
        left, right = 0, 4
        real_left, real_right = 6, 10
        
            [0,  23, 18, 5, 9, 9, 1, 4, 5, 4, 2, 7 ]
         i:  0   1   2   3  4  5  6  7  8  9  10 11
                 ^       ^        ^           ^
                 |       |        left        right
                 x       |        (current)
                 |       |        
                 |       parent
                 |       range(6,7)
                 |
                 grand-parent
                 range(6,11) - too large
        
        """
        left += self.nums_length
        right += self.nums_length
        
        res = 0
        while left <= right:
            # when left and right are equal to each other
            # it will trigger one of the below checks
            # and adds one last time to results
            if left % 2 == 1:
                # Left is currently on an odd index.
                # This means its parent value covers
                # the range (left - 1, left). We need
                # to exclude (left - 1) from our sum.
                #
                # To do this, we simply move our left
                # pointer up by 1.
                res += self.segment_tree[left]
                left += 1
            if right % 2 == 0:
                # Similar to left at an odd index,
                # right at an even index would mean
                # its parent value covers the range
                # (right, right + 1). We need to exclude
                # (right + 1) from our sum.
                #
                # To do this, we move our right pointer
                # down by 1
                res += self.segment_tree[right]
                right -= 1
            
            # left and right should both have parents that
            # cover ranges within the request
            left = left // 2
            right = right // 2

        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
