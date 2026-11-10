class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        numset = set(nums)
        length = 0
        for num in numset:
            if num-1 in numset:
                continue
            else:
                hashmap[num].append(num)
            i = num+1
            while i in numset:
                hashmap[num].append(i)
                i +=1
            length = max(length, i-num)
        return length