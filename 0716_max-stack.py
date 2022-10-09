# https://leetcode.com/problems/max-stack/
import heapq


class Node:
    def __init__(self, id: int, val: int):
        self.id = id
        self.val = val
        self.heap_node = [-self.val, -self.id]
        self.heap_node_key = tuple(self.heap_node)
        self.prev = None
        self.next = None


class MaxStack:

    DUMMY = -math.inf
    INVALID = math.inf

    def __init__(self):
        self.ids = itertools.count(start=0) # unique node IDs

        self.max_heap = []
        self.heap_node_map = {} # Dict[(-val, -id), Node]

        self.stack = Node(id=MaxStack.DUMMY, val=MaxStack.DUMMY)


    def push(self, x: int) -> None:
        node = Node(id=next(self.ids), val=x)

        # push to stack
        node.prev = self.stack
        self.stack.next = node
        self.stack = node

        # push to heap
        heapq.heappush(self.max_heap, node.heap_node)
        self.heap_node_map[node.heap_node_key] = node


    def pop(self) -> int:
        node = self.stack

        # pop from stack
        self.stack = node.prev
        self.stack.next = None
        node.prev = None

        # "pop" from heap
        del self.heap_node_map[node.heap_node_key]
        node.heap_node[1] = MaxStack.INVALID

        return node.val


    def top(self) -> int:
        return self.stack.val


    def peekMax(self) -> int:
        while self.max_heap[0][1] == MaxStack.INVALID:
            _ = heapq.heappop(self.max_heap)

        return -self.max_heap[0][0]


    def popMax(self) -> int:
        while self.max_heap[0][1] == MaxStack.INVALID:
            _ = heapq.heappop(self.max_heap)
        
        # pop from heap
        heap_node = heapq.heappop(self.max_heap)
        heap_node_key = tuple(heap_node)

        # retrieve node from map
        node = self.heap_node_map[heap_node_key]
        del self.heap_node_map[heap_node_key]

        # remove from stack
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.stack == node:
            self.stack = node.prev
        node.prev = None

        return node.val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
