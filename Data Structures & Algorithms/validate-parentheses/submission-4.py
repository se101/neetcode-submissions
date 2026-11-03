class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"}":"{", "]":"[", ")":"("}
        for string in s:
            if string in hashmap and stack:
                if stack.pop() == hashmap[string]:
                    continue
                else:
                    return False
            stack.append(string)
        return not stack
            
