# 695. Max Area of Island

## Step1

- 200_Number of Islandsと同様にISLANDのareaをカウントするように改変すれば良さそうだが、前回の問題も5分以内にはできなかったので自力ではあきらめる。
- 前回指摘された点と他解答を参考にして実装した。

```python
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        if row == 0 or col == 0:
            return 0

        max_area = 0
        WATER = 0
        ISLAND = 1
        excluded = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == WATER:
                    excluded.add((r, c))

        def get_islands_area(r: int, c: int) -> int:
            if r < 0 or r >= row or c < 0 or c >= col:
                return 0
            if (r, c) in excluded:
                return 0
            excluded.add((r, c))

            area = 1
            area += get_islands_area(r + 1, c)
            area += get_islands_area(r, c + 1)
            area += get_islands_area(r - 1, c)
            area += get_islands_area(r, c - 1)

            return area

        for r in range(row):
            for c in range(col):
                if grid[r][c] == ISLAND:
                    max_area = max(max_area, get_islands_area(r, c))

        return max_area
```

## Step2

### DFS

- 再帰のコールスタック制限を変更する[setrecursionlimit](https://docs.python.org/ja/3/library/sys.html#sys.setrecursionlimit)を確認。
- excludedにWATERを入れていたが、`grid[r][c] == WATER`の時は0を返すように変更した。

```python
import sys

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # Raise the recursion limit
        MAX_ROW, MAX_COL = 50, 50
        sys.setrecursionlimit(MAX_ROW * MAX_COL)

        max_r, max_c = len(grid), len(grid[0])
        if max_r == 0 or max_c == 0:
            return 0

        WATER = 0
        ISLAND = 1
        visited = set()

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

### BFS

```python
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_r, max_c = len(grid), len(grid[0])
        if max_r == 0 or max_c == 0:
            return 0

        WATER = 0
        ISLAND = 1
        visited = set()

        def get_island_area(start_r: int, start_c: int) -> int:
            islands = deque([(start_r, start_c)])
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

                    visited.add((next_r, next_c))
                    islands.append((next_r, next_c))
                    area += 1

            return area

        max_area = 0
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] == ISLAND and (r, c) not in visited:
                    max_area = max(max_area, get_island_area(r, c))

        return max_area
```

## union-find

- まだ自力では実装できるほど理解はしていないが、理解はすすんできた。

```python
class UnionFind:
    def __init__(self, row: int, col: int, grid: list[list[int]]):
        self.parent = {}
        self.size = {}
        self.row = row
        self.col = col
        self.max_area = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] != 1:
                    continue
                cell_id = r * col + c
                self.parent[cell_id] = cell_id
                self.size[cell_id] = 1
                self.max_area = max(self.max_area, 1)

    def find(self, i: int) -> int:
        if i not in self.parent:
            return -1

        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == -1 or root_j == -1:
            return False

        if root_i == root_j:
            return False

        if self.size[root_i] < self.size[root_j]:
            root_i, root_j = root_j, root_i
        self.parent[root_j] = root_i
        self.size[root_i] += self.size[root_j]
        self.max_area = max(self.max_area, self.size[root_i])
        return True

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_r, max_c = len(grid), len(grid[0])
        uf = UnionFind(max_r, max_c, grid)

        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] != 1:
                    continue

                current_cell = r * max_c + c

                if c + 1 < max_c and grid[r][c+1] == 1:
                    neighbor_cell = r * max_c + (c + 1)
                    uf.union(current_cell, neighbor_cell)
                
                if r + 1 < max_r and grid[r+1][c] == 1:
                    neighbor_cell = (r + 1) * max_c + c
                    uf.union(current_cell, neighbor_cell)
        
        return uf.max_area

```

## Step3

- 細かいミスが多く10分以上かかってしまうことが何度かあった。
- 1回目 9分
- 2回目 10分
- 3回目 8分
- 
