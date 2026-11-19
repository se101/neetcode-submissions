class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        freq = Counter(nums)
        res = []
        #print(freq,bucket)
        for key, val in freq.items():
            bucket[val].append(key)
        for i in range(len(bucket)-1,-1,-1):
            for item in bucket[i]:
                res.append(item)
                k-=1
                if k==0:
                    return res