class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            area = 1
            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nr, nc = qr+dr, qc+dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc]==1 and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        area+=1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = dfs(r,c)
                    res = max(res,area)
        return res