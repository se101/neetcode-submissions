class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        minutes = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh>0:
            for _ in range(len(q)):
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nr, nc = qr+dr, qc+dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1):
                        grid[nr][nc]=2
                        fresh -=1
                        q.append((nr,nc))
            minutes+=1
        
        if fresh>0:
            return -1
        else:
            return minutes

        