class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            middle = (left+right)//2
            print(left, right)
            if target==nums[middle]:
                return middle

            if nums[left]<nums[right]:
                # array is sorted
                if nums[middle]>target:
                    right-=1
                elif nums[middle]<target:
                    left+=1
                else:
                    return middle
                continue
            
            if nums[left]<=nums[middle]:
                if nums[left]<=target<=nums[middle]:
                    right=middle-1
                else:
                    left=middle+1
                continue
            if nums[middle]<=nums[right]:
                if nums[middle]<=target<=nums[right]:
                    left=middle+1
                else:
                    right=middle-1
                continue
        return -1
            

