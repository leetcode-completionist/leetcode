class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNode = {}

        # initialize doubly-linked list with
        # dummy least/most recent nodes
        self.least_recent = Node()
        self.most_recent = Node()
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent
        
        
    def __moveToMostRecent(self, node: 'Node') -> None:
        # remove from previous position
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        # add to most recent
        self.most_recent.prev.next = node
        node.prev = self.most_recent.prev
        node.next = self.most_recent
        self.most_recent.prev = node
        
        
    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        
        node = self.keyToNode[key]
        self.__moveToMostRecent(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            self.__moveToMostRecent(node)
            node.value = value
        else:
            # new key
            node = Node(key=key, value=value)
            self.__moveToMostRecent(node)
            
            # add to dict
            self.keyToNode[key] = node

            # evict if we exceed capacity
            if len(self.keyToNode.keys()) > self.capacity:
                evict = self.least_recent.next
                self.least_recent.next = self.least_recent.next.next
                self.least_recent.next.prev = self.least_recent
                del self.keyToNode[evict.key]

class Node:
    def __init__(self, key: int = -1, value: int = -1):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
