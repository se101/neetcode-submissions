class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left, right = 0, 0
        charSet = set()
        while right<len(s):
            while left<=right and s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            length = max(length, right-left+1)
            right+=1
        return length