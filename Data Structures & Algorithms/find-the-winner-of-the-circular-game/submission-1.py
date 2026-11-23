class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = collections.deque()
        for num in range(1, n+1):
            q.append(num)
        print("q", q)
        while q:
            if len(q)==1:
                return q[0]
            for _ in range(k-1):
                num = q.popleft()
                q.append(num)
            q.popleft()
         
        
