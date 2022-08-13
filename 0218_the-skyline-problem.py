from sortedcontainers import SortedDict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        This solution uses a SortedDict where the key is building positions
        and value is the maximum height at that position.
        
        After we iterate through the buildings, we will have a collection of
        skyline points (note this is not necessarily "key points" because it
        can contain multiple points in a line).
        
        We just need to iterate through the dictionary and ignore any repeated
        height points to get the final list of skyline "key points"
        """
        sorted_dict = SortedDict()
        
        # sets an initial floor of 0
        sorted_dict.setdefault(-1, 0)
        
        for left, right, height in buildings:

            if right not in sorted_dict or sorted_dict.get(right) < height:
                # find the height of the surface this building will
                # sit on (could be the floor or another building)
                #
                # we want to bisect_right in case we have the other
                # building ending on the same position. If so, we will
                # simply use the height from other building
                prev_idx = sorted_dict.bisect_right(right) - 1
                surface_height = sorted_dict.peekitem(prev_idx)[-1]
                if surface_height < height:
                    sorted_dict[right] = surface_height

            if left not in sorted_dict or sorted_dict.get(left) < height:
                # find the height of the surface this point will sit on
                #
                # we want to bisect_left because we want to immediate
                # point to the left to act as the "surface"
                prev_idx = sorted_dict.bisect_left(left) - 1
                surface_height = sorted_dict.peekitem(prev_idx)[-1]
                if surface_height < height:
                    sorted_dict[left] = height
        
            # scan through all points within current building left/right
            # to see if we need to update any previously set points.
            start = sorted_dict.bisect_left(left)
            end = sorted_dict.bisect_left(right)

            for i in range(start, end):
                point = sorted_dict.peekitem(i)
                if point[-1] < height:
                    # previously set point is a lower height
                    # we will update it to the current height
                    sorted_dict[point[0]] = height

        res = []
        
        # pop all key/value pairs into the result list
        # we skip the first key/value (i.e. (-1, 0))
        # because that is not from a building
        for pos in list(sorted_dict.keys())[1:]:
            height = sorted_dict.pop(pos)
            if res and res[-1][-1] == height:
                # if current point's height is the same
                # as previous, we can skip it.
                continue
            res.append([pos, height])

        return res
