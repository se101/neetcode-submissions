class Solution:
    def compress(self, chars: List[str]) -> int:
        k, i, j = 0, 0, 0
        while j<len(chars):
            chars[k] = chars[i]
            k+=1
            while j<len(chars) and chars[j]==chars[i]:
                j+=1
            length = j-i
            if length>1:
                for c in str(length):
                    chars[k] = c
                    k+=1
            i=j
            print("i:", i, "j:", j, "k:", k)
        return k
