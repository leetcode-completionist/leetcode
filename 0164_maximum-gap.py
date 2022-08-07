class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        We use bucket sort to achieve O(n) runtime. However,
        instead of using values as bucket index, we use a "gap" index
        to fit a value into a range where it is uniformly gapped with
        its neighbors. This allows us to look at the gap between buckets instead.
        
        For example:
        
        [4, 3, 9, 1]
        
        min = 1
        max = 9
        total_gap = (9-1) = 8 (this is the gap across the entire array)
       
        If we do a normal bucket sort, our buckets would look like:
        
                    0  1  2  3  4  5  6  7
          buckets  [1][ ][3][4][ ][ ][ ][9]
       
        However, this is no longer linear space and the num can go up
        to 10**9. Instead, we will need to limit our buckets. Keep in mind
        we ONLY need to find the maximum GAP. So we only need to keep
        enough numbers sorted to help us determine that answer.
        
        Let's summarize what we know:
        
        1. Our total gap is 8
        2. We have 4 elements, which means we have (4-1) gaps
        3. We can think of the above as:
        
           gap_0 + gap_1 + gap_2 = 8 (total_gap)

        What if we make our gap index the bucket index instead?
           
        4. We know for sure that there will be at least two buckets
           populated with >= 1 element. Why? If everything is in one
           bucket, we would never get total_gap of 8. 
        
        This leads us to an important realization:
        
        5. Our answer will always be the gap between two buckets,
           instead a gap inside elements of the same bucket. Gap between two
           buckets will always be >= gap within a single bucket.

        6. So we just need to figure out which bucket a number would go into.
           Then within each bucket, we keep track of the min/max.
           Then lastly, we will iterate through all the buckets to identify
           the maximum gap (which we know will be between two buckets).
        """
        n = len(nums)
        if n < 2:
            return 0
        
        # find the min and max in the array
        # this gives us the range that gaps will fall into
        min_num = min(nums)
        max_num = max(nums)
        total_gap = max_num - min_num
        if total_gap == 0:
            # no gap, all are equal
            return 0
        
        # if we have n elements, we have n - 1 gaps
        gap_count = n - 1
        
        # find the minimum bucket size needed.
        bucket_size = math.ceil(total_gap / gap_count)
        
        # keep track of min/max at each bucket
        bucket_min = [float("inf")] * n
        bucket_max = [float("-inf")] * n
        
        # assign our numbers to a bucket
        for num in nums:
            bucket_idx = (num - min_num) // bucket_size
            bucket_min[bucket_idx] = min(bucket_min[bucket_idx], num)
            bucket_max[bucket_idx] = max(bucket_max[bucket_idx], num)
        
        # iterate through each bucket
        # while keeping track of the max gap between buckets
        res = 0
        
        prev_bucket_max = bucket_max[0]
        for i in range(1, n):
            if bucket_min[i] == float("inf"):
                # we didn't put anything in this bucket, skip
                continue
            
            # see if gap between this bucket and previous bucket
            # is larger than result
            res = max(res, bucket_min[i] - prev_bucket_max)
            prev_bucket_max = bucket_max[i]
        
        return res
