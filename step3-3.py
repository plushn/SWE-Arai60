from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        ISLAND = "1"
        WATER = "0"
        
        def isIslands(r: int, c: int) -> None:
            islands = deque([(r, c)])
            
            while islands:
                current_r, current_c = islands.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    next_r, next_c = current_r + dr, current_c + dc
                    if 0 <= next_r < row and 0 <= next_c < col and (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        islands.append((next_r, next_c))
        
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == WATER:
                    visited.add((r, c))
        islands_count = 0
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited:
                    visited.add((r, c))
                    islands_count += 1
                    isIslands(r, c)
        return islands_count
