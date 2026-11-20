class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, k
        res = [max(nums[:k])]
        while right<len(nums):
            if nums[right]>res[-1]:
                res.append(nums[right])
            elif nums[left]==res[-1]:
                res.append(max(nums[left+1:right+1]))
            else:
                res.append(res[-1])
            left+=1
            right+=1
            #print(res)
        return res