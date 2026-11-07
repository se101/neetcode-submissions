class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = Counter(t)
        window = {}
        have = 0
        need = len(countT)
        res = ""
        reslen = float("inf")
        left, right = 0,0
        while right<len(s):
            window[s[right]] = 1+window.get(s[right],0)
            if s[right] in countT and window[s[right]]==countT[s[right]]:
                have+=1
            while have==need:
                if (right-left+1)<reslen:
                    res = s[left:right+1]
                    reslen = (right-left+1)
                window[s[left]]-=1
                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    have-=1
                left+=1
            right+=1
        return res