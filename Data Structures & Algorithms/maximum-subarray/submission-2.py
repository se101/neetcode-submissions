class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumN, res = nums[0], nums[0]
        for i in range(1,len(nums)):
            if (sumN+nums[i])>nums[i]:
                sumN = sumN+nums[i]
            else:
                sumN = nums[i]
            res = max(res,sumN)
        return res 