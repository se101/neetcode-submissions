class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        res = ""
        length = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i,len(s)):
                if s[i]==s[j] and (j-i<3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1>length:
                        res = s[i:j+1]
                        length = j-i+1
                #print("dp:", dp)
        return res