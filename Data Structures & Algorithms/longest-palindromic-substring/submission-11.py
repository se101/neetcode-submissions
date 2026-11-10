class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        for i in range(len(s)):
            #print("i:", i)
            left, right = i, i
            while s[left]==s[right]:
                if len(s[left:right+1])>length:
                    res = s[left:right+1]
                    length = len(s[left:right+1])
                if left>0 and right<len(s)-1:
                    left-=1
                    right+=1
                else:
                    break

            if i>0:
                left, right = i-1, i
                while s[left]==s[right]:
                    if len(s[left:right+1])>length:
                        res = s[left:right+1]
                        length = len(s[left:right+1])
                    if left>0 and right<len(s)-1:
                        left-=1
                        right+=1
                    else:
                        break
            #print(res, left, right)
        return res