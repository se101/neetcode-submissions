class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left, right = 0, 1
        if s=="":
            return 0
        if len(s)==1:
            return 1
        charset = set(s[left])
        while left<right and right<len(s):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            right+=1
            length = max(length, len(charset))
        return length


        