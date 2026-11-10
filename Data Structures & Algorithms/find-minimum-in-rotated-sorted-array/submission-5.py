class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        minVal = float("inf")
        while left<=right:
            if nums[left]<=nums[right]:
                minVal = min(minVal, nums[left])
            middle = (left+right)//2
            minVal = min(minVal, nums[middle])
            if nums[left]<=nums[middle]:
                left = middle+1
            else:
                right = middle-1
        return minVal