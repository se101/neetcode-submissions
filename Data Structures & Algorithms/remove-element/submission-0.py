class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        extras = []
        for num in nums:
            if num!=val:
                extras.append(num)
        for i in range(len(extras)):
            nums[i] = extras[i]
        return len(extras)