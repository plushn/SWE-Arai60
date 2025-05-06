class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        if row == 0 or col == 0:
            return 0

        uf = UnionFind(row * col)
        islands_count = row * col

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '0':
                    islands_count -= 1
                    continue

                current_index = r * col + c
                directions = [(1, 0), (0, 1)]
                for dr, dc in directions:
                    next_r, next_c = r + dr, c + dc
                    if (0 <= next_r < row and
                        0 <= next_c < col and
                        grid[next_r][next_c] == '1'):
                        neighbor_index = next_r * col + next_c
                        if uf.union(current_index, neighbor_index):
                            islands_count -= 1

        return islands_count
