from functools import cmp_to_key

class Solution:
    """
    This solution implements a custom sorting comparator, so that our
    nums will be sorted in the order that generates the largest number.
    
    For example, given 34323 and 3432, how should we compare them so we
    will end up with 3432|34323 instead of 34323|3432?
       
    First we can just iterate both string one at a time to compare the digits.
    
        a: 3432
        b: 34323
           ====
        i: 01234
        
    When we reach index 3, we've exhausted all digits in 'a'. But we still don't
    know if a or b should come first. At least we know they are not equal.
    What if we extend 'a' and keep comparing:
    
        a: 3432|3432
        b: 3432|3
           ====|=
        i: 0123|45678
    
    Now we've exhausted all of 'b'. And we still don't know if a or b should come
    first. So we extend 'b' this time and keep comparing:
    
        a: 3432|3|432
        b: 3432|3|34323
           ====|=|<
        i: 0123|4|56789
    
    We now see that a is larger at index 5. This comparison tells us if we should
    put 'a' before 'b' for a largest number. So we will return -1 in our comparator.
    """
    def largestNumber(self, nums: List[int]) -> str:
        # define a custom comparator
        def compare(a, b):
            s_a, s_b = str(a), str(b)
            
            while s_a or s_b:
                # if we used up number "a", we will replenish it
                # with another "a"
                if not s_a:
                    s_a = str(a)
                    
                # if we used up number "b", we will replenish it
                # with another "b"
                if not s_b:
                    s_b = str(b)
                
                n = min(len(s_a), len(s_b))

                for i in range(n):
                    if s_a[i] < s_b[i]:
                        # a's digit is smaller, it should go later
                        return 1
                    elif s_a[i] > s_b[i]:
                        # a's digit is larger, it should go first
                        return -1
                    else:
                        continue
            
                # trim the strings down to where we ended our comparisons
                #
                # if both strings are empty, then they are equal
                # if one string is not empty, we restart the comparison
                # again until we find a larger digit between the two numbers
                s_a = s_a[n:]
                s_b = s_b[n:]
            
            # a and b are equal in length and value
            return 0

        # sort nums by the order they should appear in
        nums = sorted(nums, key=cmp_to_key(compare))

        if nums[0] == 0:
            # edge case where the first element is 0
            # this means no other element is larger
            # and we can safely return a "0" as the result
            return "0"
        
        return "".join([str(i) for i in nums])
