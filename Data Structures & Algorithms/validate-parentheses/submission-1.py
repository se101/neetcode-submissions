class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(", "}":"{", "]":"["}
        arr = []
        for c in s:
            if c not in valid:
                arr.append(c)
            else:
                if len(arr)>0 and valid[c]==arr[-1]:
                    arr.pop()
                else:
                    return False
        return True if len(arr)==0 else False
