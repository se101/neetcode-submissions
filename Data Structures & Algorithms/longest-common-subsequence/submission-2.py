class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2)<len(text1):
            text1, text2 = text2, text1
        dp = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        for i in range(len(text2)-1,-1,-1):
            for j in range(len(text1)-1,-1,-1):
                if text2[i]==text1[j]:
                    #print("***Matching***")
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
                #print("indexes:",i,j)
                #print(dp)
        return dp[0][0]