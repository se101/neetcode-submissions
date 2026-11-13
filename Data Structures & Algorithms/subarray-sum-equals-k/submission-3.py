class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        prefix = prefix[1:]
        hashmap = {}
        hashmap[0] = 1
        count = 0
        for i in range(len(prefix)):
            if prefix[i]-k in hashmap:
                count += hashmap[prefix[i]-k]
            hashmap[prefix[i]] = 1 + hashmap.get(prefix[i], 0)
        return count

            
