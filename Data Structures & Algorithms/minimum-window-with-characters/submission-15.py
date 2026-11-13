class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        countS = {}
        have = 0
        need = len(set(t))
        left, right = 0, 0
        length = float("inf")
        res = ""
        while right<len(s):
            if s[right] in countT:
                countS[s[right]] = 1 + countS.get(s[right],0)
                if countS[s[right]] == countT[s[right]]:
                    have +=1
            while have == need:
                if length>right-left+1:
                    res = s[left:right+1]
                    length = len(res)
                if s[left] in countS:
                    countS[s[left]]-=1
                    if countS[s[left]]<countT[s[left]]:
                        have-=1
                left+=1
            right+=1
        return res
