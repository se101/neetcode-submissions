class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0]*26
        for c in s1:
            count1[ord(c)-ord('a')]+=1
        print(count1)
        count2 = [0]*26
        k = len(s1)
        left, right=0,0
        while right<len(s2):
            c=s2[right]
            count2[ord(c)-ord('a')]+=1
            if right-left+1>k:
                count2[ord(s2[left])-ord('a')]-=1
                left+=1
            if count1==count2:
                return True
            right+=1
        return False