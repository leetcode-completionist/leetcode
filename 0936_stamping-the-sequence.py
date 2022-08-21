# https://leetcode.com/problems/stamping-the-sequence/
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp_len = len(stamp)
        target_len = len(target)
        
        def canStamp(sub_target: str) -> bool:
            # checks whether or not we can stamp
            # current sub-target.
            for i in range(stamp_len):
                # if at any given point we come across a mismatched
                # char (that is not a wildcard), we know we cannot
                # stamp current subtarget
                if sub_target[i] != stamp[i] and sub_target[i] != "?":
                    return False
            
            # all chars are matching or wildcard, we can stamp
            return True
    
        res = []
        
        max_moves = 10 * target_len
        move = 0
        while move < max_moves:            
            # keep track of whether or not we
            # made a move this iteration
            old_move = move
            # keep stamping from target to wildcards
            # until we run out of moves or we
            # are unable to stamp further
            for i in range(target_len - stamp_len + 1):
                # we must stamp within the boundaries
                if canStamp(target[i:i + stamp_len]):
                    move += 1
                    res.append(i)
                    
                    # set stamped chars to wildcard
                    target = (target[:i] +
                              "?" * stamp_len +
                              target[i + stamp_len:])
                    
                    # check if target is fully stamped
                    if target == "?" * target_len:
                        # the entire target has been
                        # stamped, we return our results
                        # in reverse order
                        return res[::-1]

            if old_move == move:
                # we weren't able to stamp during this
                # iteration.
                # there is no way to completely stamp the target
                return []
        
        # we weren't able to stamp within the max moves
        return []
