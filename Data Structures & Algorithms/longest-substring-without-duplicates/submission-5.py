class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left= 0
        charset = set()
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            length = max(length, right-left+1)
        return length


        