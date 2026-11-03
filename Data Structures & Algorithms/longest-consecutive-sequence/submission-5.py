class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = defaultdict(list) # {100: [100,], 200: [200,], 1:[1,2,3,4]}
        setnums = set(nums)
        maxcount = 0
        for num in nums:
            if num-1 in setnums:
                continue
            else:
                res[num].append(num)
            
            temp = num+1
            while temp in setnums:
                res[num].append(temp)
                temp = temp+1
            
            maxcount = max(maxcount,len(set(res[num])))
        return maxcount