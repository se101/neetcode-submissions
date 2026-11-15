class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()
        for num in range(1,n+1):
            q.append(num)
        while len(q)>1:
            for _ in range(k-1):
                num = q.popleft()
                q.append(num)
            q.popleft()
        return q[0]
