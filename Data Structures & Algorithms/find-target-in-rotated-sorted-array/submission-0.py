class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<= right:
            middle = (left+right)//2
            if target == nums[middle]:
                return middle
            # left sorted part [3,4,5][1,2]
            if nums[middle]>=nums[left]:
                if target > nums[middle] or target < nums[left]:
                    left = middle+1
                else:
                    right = middle-1
            # right sorted part
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle-1
                else:
                    left = middle+1
        return -1