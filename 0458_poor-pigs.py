class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # calculate the maximum number of trials we can perform
        trials = minutesToTest // minutesToDie
        
        # for any given pig, there are trials + 1 different possible states:
        #
        # die on 1st, or
        # die on 2nd, or
        # ...
        # die on nth trial, or
        # not die at all
        #
        # there will be (trials + 1)^pigs possible states, each can have its own
        # bucket.
        #
        # therefore we will find the minimum number of pigs such that:
        #
        #     buckets <= (trials + 1) ^ pigs
        #
        #     log(buckets) <= log(trials + 1) * pigs
        #
        #     log(buckets) / log(trials + 1) <= pigs
        #
        #     ceil(log(buckets) / log(trials + 1)) = pigs
        
        return math.ceil(math.log(buckets) / math.log(trials + 1))
