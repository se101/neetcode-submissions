class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        charset = set(s)
        for c in charset:
            left, count = 0, 0
            for right in range(len(s)):
                if s[right]==c:
                    count+=1
                if ((right-left+1)-count)>k:
                    if s[left]==c:
                        count-=1
                    left+=1
                length = max(length, right-left+1)
        return length
