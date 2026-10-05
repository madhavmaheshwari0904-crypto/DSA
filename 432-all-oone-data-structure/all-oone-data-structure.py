from sortedcontainers import SortedDict

class AllOne:
    def __init__(self):
        # Maps key -> its current count
        self.key_count = {}
        # SortedDict maps count -> set of keys sharing that count
        self.count_keys = SortedDict()

    def inc(self, key: str) -> None:
        curr_cnt = self.key_count.get(key, 0)
        new_cnt = curr_cnt + 1
        self.key_count[key] = new_cnt
        
        # Remove key from its old count bucket
        if curr_cnt > 0:
            self.count_keys[curr_cnt].remove(key)
            if not self.count_keys[curr_cnt]:
                del self.count_keys[curr_cnt]
                
        # Add key to its new count bucket
        if new_cnt not in self.count_keys:
            self.count_keys[new_cnt] = set()
        self.count_keys[new_cnt].add(key)

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        
        curr_cnt = self.key_count[key]
        new_cnt = curr_cnt - 1
        
        # Remove key from its current count bucket
        self.count_keys[curr_cnt].remove(key)
        if not self.count_keys[curr_cnt]:
            del self.count_keys[curr_cnt]
            
        # Update or delete key count
        if new_cnt == 0:
            del self.key_count[key]
        else:
            self.key_count[key] = new_cnt
            if new_cnt not in self.count_keys:
                self.count_keys[new_cnt] = set()
            self.count_keys[new_cnt].add(key)

    def getMaxKey(self) -> str:
        if not self.count_keys:
            return ""
        # peekitem(-1) gives the largest count (last item in SortedDict)
        max_cnt, keys = self.count_keys.peekitem(-1)
        return next(iter(keys))

    def getMinKey(self) -> str:
        if not self.count_keys:
            return ""
        min_cnt, keys = self.count_keys.peekitem(0)
        return next(iter(keys))