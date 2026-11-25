import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            candidate = random.choice(nums)
            count = nums.count(candidate)
            if count > n/2:
                return candidate