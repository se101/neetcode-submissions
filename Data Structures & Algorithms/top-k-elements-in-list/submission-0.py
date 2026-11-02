class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = dict(sorted(count.items(), key = lambda item: item[1], reverse = True))
        return list(count.keys())[:k]