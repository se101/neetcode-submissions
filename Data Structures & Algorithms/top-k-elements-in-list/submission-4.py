class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort 
        hashmap = {}
        bucket = [[] for _ in range(len(nums)+1)]
        res = []
        for num in nums:
            hashmap[num] = 1+hashmap.get(num, 0)
        #print(hashmap)
        # {1:1, 2:2, 3:3}
        for key, item in hashmap.items():
            bucket[item].append(key)
        #print(bucket)
        for i in range(len(bucket)-1, -1, -1):
            count = len(bucket[i])
            while k and count:
                res.append(bucket[i][count-1])
                k-=1
                count-=1
                #print(k)
        return res