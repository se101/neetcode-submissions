class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1,text2 = s,s[::-1]
        dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]