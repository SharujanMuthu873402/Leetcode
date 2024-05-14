class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pairs = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.pairs:
            self.pairs.move_to_end(key)
            return self.pairs[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.pairs:
            del self.pairs[key]
        
        if len(self.pairs) == self.capacity:
            self.pairs.popitem(last = False)
        
        self.pairs[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)