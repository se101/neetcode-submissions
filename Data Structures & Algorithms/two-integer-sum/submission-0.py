class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # {3:0, 4:1, 5:2, 6:3}
        for i, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num], i]
            else:
                hashmap[num] = i