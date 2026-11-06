class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        res = ""
        while p1<len(word1) and p1<len(word2):
            res+=word1[p1]
            res+=word2[p1]
            p1+=1
        if len(word1)>p1:
            res+=word1[p1:]
        if len(word2)>p1:
            res+=word2[p1:]
        return res