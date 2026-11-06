class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        if len(s)==1:
            return s
        for i in range(0,len(s)):
            left, right = i, i
            while left>=0 and right<len(s):
                if s[left]==s[right]:
                    if len(s[left:right+1])>length:
                        res = s[left:right+1]
                        length = len(res)
                    left-=1
                    right+=1
                else:
                    break
                #print(res)
              
            if i<(len(s)-1) and s[i]==s[i+1]:
                left, right = i, i+1
                while left>=0 and right<len(s):
                    if s[left]==s[right]:
                        if len(s[left:right+1])>length:
                            res = s[left:right+1]
                            length = len(res)
                        left-=1
                        right+=1
                    else:
                        break
                    
            #print(s[i],res)
        return res

