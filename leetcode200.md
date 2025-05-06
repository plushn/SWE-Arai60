# 200. Number of Islands

## Step1

- 5分以内には解けなさそうなのですぐに断念。
- geminiと相談しながら実装してみた。方針としてはDFS、BFS、UnionFindがあるようだが、まずはDFSで実装した。

```python
from collections import deque
import copy

class Solution:
    def isIslands(
            self, grid: list, r: int, c: int, row: int, col: int
        ) -> None:
        islands = deque([(r, c)])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while islands:
            current_r, current_c = islands.pop()
            for dr, dc in directions:
                next_r, next_c = current_r + dr, current_c + dc
                if 0 <= next_r < row and 0 <= next_c < col and grid[next_r][next_c] == "1":
                    grid[next_r][next_c] = "0"
                    islands.append((next_r, next_c))

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        chacking_grid = copy.deepcopy(grid)
        row = len(grid)
        col = len(grid[0])
        islands_count = 0

        for r in range(row):
            for c in range(col):
                if chacking_grid[r][c] == "1":
                    islands_count += 1
                    chacking_grid[r][c] = "0"
                    self.isIslands(chacking_grid, r, c, row, col)

        return islands_count

```

## Step2

- step1では新たなgridをコピーして実装したが、setを利用する方法もあるようだ。
- 先頭と末尾を取り出すのが高速なのでdequeを利用したが、listでも十分との意見もあった。
- WATER = "0" 、LAND = "1" のように具体的に定義するように変更した。
- 別のメソッドとして定義したが、おそらく再利用することはないと思わるので関数内関数にすることで引数を減らし可読性を高くした。
- DFSはwhileではなく再帰で実装しなおしてみた。
- DFS、BFSそれぞれ実装してみた。
- DFS,BFSともに時間計算量 O(rc) 空間計算量 O(rc) r: rowの長さ c: colの長さ

### DFS

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col, row = len(grid[0]), len(grid)
        if col == 0 or row == 0:
            return 0

        def isIsland(r:int, c:int) -> None:
            islands = [(r, c)]
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            current_r, current_c = islands.pop()
            for d_r, d_c in directions:
                next_r, next_c = current_r + d_r, current_c + d_c
                if 0 <= next_r < row and 0 <= next_c < col and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    islands.append((next_r, next_c))
                    isIsland(next_r, next_c)
                    
        ISLAND = "1"
        WATER = "0"
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == WATER:
                    visited.add((r, c))


        islands_count = 0
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited:
                    islands_count += 1
                    isIsland(r, c)
        return islands_count
```

### BFS

- こちらはdequeを使用して先頭からpopできるようにした。

```python
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col, row = len(grid[0]), len(grid)
        if col == 0 or row == 0:
            return 0

        def isIsland(r:int, c:int) -> None:
            islands = deque([(r, c)])
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while islands:
                current_r, current_c = islands.popleft()
                for d_r, d_c in directions:
                    next_r, next_c = current_r + d_r, current_c + d_c
                    if 0 <= next_r < row and 0 <= next_c < col and (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        islands.append((next_r, next_c))

        ISLAND = "1"
        WATER = "0"
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == WATER:
                    visited.add((r, c))

        islands_count = 0
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited:
                    islands_count += 1
                    isIsland(r, c)
        return islands_count

```

### UnionFind

- union findという方法で解いている方もいた。自力で実装できるレベルでは理解できておらず、後日3回自力で実装できるように練習したい。
  - island_gridをgrid総数`row * col`で初期化
  - gridがWATERの場合、islands_countを-1する。
  - gridがISLANDでその隣接gridもISLANDの場合、結合してislands_countを-1する。

## Step3

- なんとか10分で実装できるようになったが、細かいミスが残ってしまうのでそこに時間がかかってしまった。
- 1回目 13分
- 2回目 11分
- 3回目 10分
