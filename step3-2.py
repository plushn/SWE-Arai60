class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        ISLAND = "1"
        WATER = "0"
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == WATER:
                    visited.add((r, c))
        
        def isIslands(r: int , c: int) -> None:
            islands = [(r, c)]
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while islands:
                current_r, current_c = islands.pop()
                for dr, dc in directions:
                    next_r, next_c = current_r + dr, current_c + dc
                    if 0 <= next_r < row and 0 <= next_c < col and (next_r, next_c) not in visited:
                        islands.append((next_r, next_c))
                        visited.add((next_r, next_c))
            
        islands_count = 0
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited:
                    islands_count += 1
                    visited.add((r, c))
                    isIslands(r, c)
        
        return islands_count
