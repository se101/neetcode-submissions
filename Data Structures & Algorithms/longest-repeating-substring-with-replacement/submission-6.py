class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        maxF, res = 0, 0
        left, right = 0,0
        for c in s:
            hashmap[c] = 1 + hashmap.get(c,0)
            maxF = max(maxF, hashmap[c])
            if ((right-left+1)-maxF)<=k:
                res = max(res,right-left+1)
            else:
                hashmap[s[left]]-=1
                left+=1
            right+=1
        return res
