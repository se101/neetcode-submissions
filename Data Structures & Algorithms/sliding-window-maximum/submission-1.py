class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        maxVal = float("-inf")
        res = []
        while right<k:
            maxVal = max(maxVal, nums[right])
            right+=1
        left+=1
        res.append(maxVal)
        while right<len(nums):
            if nums[left-1] == maxVal:
                maxVal = max(nums[left:right+1])
            else:
                maxVal = max(maxVal, nums[right])
            res.append(maxVal)
            right+=1
            left+=1
        return res
