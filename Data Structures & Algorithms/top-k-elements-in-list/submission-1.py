class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) #{1:1, 2:2, 3:3}
        freq = [[] for _ in range(len(nums)+1)] #[[],[1],[2],[3]]
        for i,n in count.items():
            freq[n].append(i)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
       