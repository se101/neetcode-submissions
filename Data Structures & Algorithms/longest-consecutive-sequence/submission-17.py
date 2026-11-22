class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            count = 1
            if num-1 in nums:
                continue
            while num+1 in nums:
                count+=1
                num = num+1
            if count>res:
                res = count
        return res