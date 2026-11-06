class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.hashmap.get(key, [])
        
        left, right = 0, len(values)-1
        while left<=right:
            middle = (left+right)//2
            if values[middle][1]<=timestamp:
                res = values[middle][0]
                left = middle+1
            else:
                right=middle-1
        return res
