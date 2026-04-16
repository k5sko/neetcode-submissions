class TimeMap:

    def __init__(self):
        self.key_time = dict() # gets the value for a (key, timestamp) tuple
        self.key = dict() # gets all timestamps for a key

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_time[(key, timestamp)] = value
        if key not in self.key:
            self.key[key] = list()
        self.key[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key:
            return ""
        
        times = self.key[key]

        # Binary search over times to get the greatest time <= timestamp
        l, r = 0, len(times) - 1
        while l <= r: # breaks when l > r
            m = (l+r)//2
            if timestamp == times[m]:
                r = m
                break
            elif timestamp < times[m]:
                r = m - 1
            else:
                l = m + 1
        # we know 

        return "" if r < 0 else self.key_time[(key, times[r])]