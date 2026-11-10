class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
        text1 = s
        text2 = s[::-1]
       
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[len(s)][len(s)]

                