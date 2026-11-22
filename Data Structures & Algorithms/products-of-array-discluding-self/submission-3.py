class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for num in nums:
            res.append(res[-1]*num)
        res = res[:-1]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res