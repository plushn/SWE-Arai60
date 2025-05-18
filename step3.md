```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ISLAND = 1
        WATER = 0
        max_row, max_col = len(grid), len(grid[0])

        def get_area(r: int, c: int) -> int:
            if not(0 <= r < max_row and 0 <= c < max_col):
                return 0
            if not((r, c) not in visited and grid[r][c] == ISLAND):
                return 0
            visited.add((r, c))
            
            area = 1
            area += get_area(r + 1, c)
            area += get_area(r, c + 1)
            area += get_area(r - 1, c)
            area += get_area(r, c - 1)

            return area

        max_area = 0
        for r in range(max_row):
            for c in range(max_col):
                if grid[r][c] == ISLAND:
                    max_area = max(max_area, get_area(r, c))
        return max_area
```

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        WATER = 0
        ISLAND = 1
        max_r, max_c = len(grid), len(grid[0])

        def get_island_area(r: int, c: int) -> int:
            if not(0 <= r < max_r and 0 <= c < max_c):
                return 0
            if not((r, c) not in visited and grid[r][c] == ISLAND):
                return 0
            visited.add((r, c))
            
            area = 1
            area += get_island_area(r + 1, c)
            area += get_island_area(r, c + 1)
            area += get_island_area(r - 1, c)
            area += get_island_area(r, c - 1)
            return area
        
        max_area = 0
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] == ISLAND:
                    max_area = max(max_area, get_island_area(r, c))
        return max_area
```

```python
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_r, max_c = len(grid), len(grid[0])
        WATER = 0
        ISLAND = 1
        visited = set()

        def get_island_area(start_r: int, start_c: int) -> int:
            islands = deque()
            islands.append((start_r, start_c))
            visited.add((start_r, start_c))

            area = 1
            while islands:
                current_r, current_c = islands.popleft()
                
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    next_r, next_c = current_r + dr, current_c + dc
                    if not(0 <= next_r < max_r and 0 <= next_c < max_c):
                        continue
                    if not((next_r, next_c) not in visited and grid[next_r][next_c] == ISLAND):
                        continue
                    islands.append((next_r, next_c))
                    visited.add((next_r, next_c))
                    area += 1
            
            return area
        
        max_area = 0
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] == ISLAND and (r, c) not in visited:
                    max_area = max(max_area, get_island_area(r, c))
        return max_area
```
