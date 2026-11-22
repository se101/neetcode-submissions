class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        hashmap = {}
        def dp(i,k,prev,prev_count):
            if (i,k,prev,prev_count) in hashmap:
                return hashmap[(i,k,prev,prev_count)]
            if k<0:
                return float("inf")
            if i==len(s):
                return 0
            if s[i]==prev:
                add = 1 if prev_count in [1,9,99] else 0
                res = add + dp(i+1, k, prev, prev_count+1)
            else:
                res = min(
                    1+dp(i+1,k,s[i],1),
                    dp(i+1,k-1,prev,prev_count)
                )
            hashmap[(i,k,prev,prev_count)] = res
            return res
        return dp(0,k,"",0)