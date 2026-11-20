class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])
        hashmap = {}
        hashmap[0]=1
        res = 0
        for i in range(len(nums)):
            if prefix[i]-k in hashmap:
                res+=hashmap[prefix[i]-k]
            hashmap[prefix[i]] = 1+hashmap.get(prefix[i],0)
        return res