class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Implementation of union find.
        
        The start of any consecutive sequence will be the "representative"
        of a disjoint set.
        """
        if not nums:
            return 0
        
        # Initialize parents dict where every node is parent of itself
        parents = {}
        for num in nums:
            parents[num] = num
        
        def union(x, y):
            # unions "y" into "x"
            #
            # this is done by setting the x_root as the
            # parent of y_root
            parents[(findAndCompress(y))] = findAndCompress(x)
        
        def findAndCompress(x: int) -> int:
            """
            Given a node, traverse upwards until we reach
            a root node.
            
            Additionally, for all nodes we encounter,
            we compress paths to point directly to root.
            """
            nodes = []
            root = parents[x]
            while root in parents and parents[root] != root:
                # there is a higher node
                # so we add current node to the list
                # and continue upwards
                nodes.append(root)
                root = parents[root]
            
            # now we know what the root is as well
            # as all the nodes that we can point to the root
            for node in nodes:
                # compress path from node to root
                parents[node] = root
                
            return root
        
        # For each number, union itself with (n - 1)
        for num in parents:
            if num - 1 in parents:
                union(num - 1, num)        
        
        # For each sequence root (i.e. start of a sequence), we increase
        # the count
        counts = defaultdict(lambda: 0)
        for num in parents.keys():
            counts[findAndCompress(num)] += 1
        
        return max(counts.values())
