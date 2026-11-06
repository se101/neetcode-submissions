class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        left, right = 0, len(s1)-1
        while right<len(s2):
            if count == Counter(s2[left:right+1]):
                return True
            left+=1
            right+=1
        return False