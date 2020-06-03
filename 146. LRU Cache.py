#https://leetcode.com/problems/lru-cache/
class LRUCache:

    def __init__(self, capacity: int):
        self.dq = collections.deque()
        self.hashmap = collections.defaultdict(int)
        self.capacity = capacity
        self.size = 0

        

    def get(self, key: int) -> int:
        try:
            self.dq.remove(key)
            self.dq.append(key)
            return self.hashmap[key]
        except ValueError:
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            x = self.hashmap[key]
            self.hashmap[key] = value
            self.dq.remove(key)
            self.dq.append(key)
        except ValueError:
            if self.size != self.capacity:
                self.hashmap[key] = value
                self.size += 1
                self.dq.append(key)
            else:
                x = self.dq.popleft()
                self.dq.append(key)
                self.hashmap[key] = value
             
            
            
