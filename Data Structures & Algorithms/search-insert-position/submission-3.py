class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right, middle = 0, len(nums)-1, 0 
        while left<=right:
            middle = (left+right)//2
            if target>nums[middle]:
                left = middle+1
            elif target<nums[middle]:
                right = middle-1
            else:
                return middle
        print(nums[middle], middle)
        if nums[middle]<target:
            return middle+1
        else:
            return middle 