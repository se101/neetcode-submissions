class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        length = 0
        for i in range(len(s)):
            #print("i:", i)
            left, right = i, i
            while s[left]==s[right]:
                #print("first loop:", s[left], s[right], left, right)
                if right-left+1>length:
                    res = s[left:right+1]
                    length = right-left+1
                #print("res:", res)
                if left>0 and right<len(s)-1:
                    left-=1
                    right+=1
                else:
                    break
                
            if i<len(s)-1 and s[i]==s[i+1]:
                left, right = i,i+1
                while s[left]==s[right]:
                    #print("second loop:", s[left], s[right])
                    if right-left+1>length:
                        res = s[left:right+1]
                        length = right-left+1
                    if left>0 and right<len(s)-1:
                        left-=1
                        right+=1
                    else:
                        break
        return res
