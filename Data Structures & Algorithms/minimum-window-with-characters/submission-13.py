class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        need = len(set(t))
        countT = Counter(t)
        countS = {}
        left = 0
        res = ""
        length = float("inf")
        for right in range(len(s)):
            if s[right] in countT:
                countS[s[right]] = 1+countS.get(s[right],0)
                if countS[s[right]]==countT[s[right]]:
                    have+=1
                while have==need:
                    if len(s[left:right+1])<length:
                        res = s[left:right+1]
                        length = right-left+1
                    if s[left] in countS:
                        countS[s[left]]-=1
                        if countS[s[left]]<countT[s[left]]:
                            have-=1
                    left+=1
            #print(s[left:right+1], countS, "have:", have, "res:", res)
        return res
            
