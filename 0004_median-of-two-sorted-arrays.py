class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shortNums = nums1
        longNums = nums2
        if len(nums2) < len(nums1):
            shortNums, longNums = longNums, shortNums
            
        l = 0
        r = len(shortNums)
        while (l <= r):
            shortPartition = int((l + r) / 2)
            shortLeft = shortNums[shortPartition - 1] if shortPartition > 0 else float('-inf')
            shortRight = shortNums[shortPartition] if shortPartition < len(shortNums) else float('inf')

            longPartition = int((len(shortNums) + len(longNums))/ 2) - shortPartition
            longLeft = longNums[longPartition - 1] if longPartition > 0 else float('-inf')
            longRight = longNums[longPartition] if longPartition < len(longNums) else float('inf')
            
            if shortLeft > longRight:
                # we went too far right
                r = shortPartition - 1
                continue
            elif shortRight < longLeft:
                # we went too far left
                l = shortPartition + 1
                continue
            
            # we found the right partitions
            if (len(shortNums) + len(longNums)) % 2 == 0:
                return (max(shortLeft, longLeft) + min(shortRight, longRight)) / 2
            else:
                return min(shortRight, longRight)
                
        # we should never get here                
        raise Exception("invalid state")
        
    
