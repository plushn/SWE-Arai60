class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        if row == 0 or col == 0:
            return 0
        ISLAND = "1"
        WATER = "0"

        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == WATER:
                    visited.add((r, c))
        
        def isIsland(r: int, c:int) -> None:
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            islands = [(r, c)]

            while islands:
                current_r, current_c = islands.pop()
                for d_r, d_c in directions:
                    next_r, next_c = current_r + d_r, current_c + d_c
                    if 0 <= next_r < row and 0 <= next_c < col and (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        islands.append((next_r, next_c))
        
        island_count = 0
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited:
                    island_count += 1
                    isIsland(r, c)
        return island_count
