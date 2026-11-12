class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, right = 0,0
        length = 0
        while right<len(s):
            while left<right and s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            if (right-left+1)>length:
                length = right-left+1
            right+=1
        return length
