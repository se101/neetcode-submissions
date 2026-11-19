class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs:
            for i in range(len(res)):
                if i==len(s):
                    res = res[:i]
                    break
                if s[i]==res[i]:
                    continue
                else:
                    res = res[:i]
                    break
        return res
