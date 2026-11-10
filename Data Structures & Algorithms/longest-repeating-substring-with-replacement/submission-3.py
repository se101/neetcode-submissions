class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left, right = 0,0
        maxF, res = 0, 0
        while right<len(s):
            hashmap[s[right]] = 1 + hashmap.get(s[right],0)
            maxF = max(maxF, hashmap[s[right]])
            length = right-left+1
            if length-maxF<=k:
                #print(length, maxF, s[left:right+1])
                res = max(res, length)
                right+=1
            else:
                hashmap[s[left]]-=1
                left+=1
                right+=1
            #print(hashmap)
        return res
