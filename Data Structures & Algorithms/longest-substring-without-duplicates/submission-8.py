class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right=0, 0
        chars = set()
        res = 0
        while right<len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            res = max(res,right-left+1)
            right+=1
        return res