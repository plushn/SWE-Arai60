# 323. Number of Connected Components in an Undirected Graph

## Step1

- まずは`edges`の管理の仕方がわからなかった。方針としてはこれまでと同様にDFSやBFS、union-findで回答可能かなと思われる。
- `edges`は各nodeのlistを作成し、そのnodeが連結しているnodeのlistを作成していく。
- 時間がかかりそうなので他の回答を参考に再帰を使ってDFSで作成。
- 時間・空間計算量O(N + E) N: nodeの数 E: edgeの数

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = set()
        components_count = 0

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def traverse_component(start_node: int) -> None:
            if start_node in visited:
                return 
            visited.add(start_node)
            for next_node in graph[start_node]:
                traverse_component(next_node)

        for start_node in range(n):
            if start_node in visited:
                continue
            components_count += 1
            traverse_component(start_node)
        
        return components_count
```

## Step2

### DFS

- graphをadjacency_list(adjacency: 隣接)に変更
- start_nodeは有向グラフのように感じられるとの意見があるためnode1, node2に変更
- components_count, visitedの位置を読みやすいように使用する直前に変更し、変数名もnums_componentsに変更

```python
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
        
        visited = set()
        def traverse_component(node: int) -> None:
            if node in visited:
                return 
            visited.add(node)
            for adjacent_node in adjacency_list[node]:
                traverse_component(adjacent_node)

        num_components = 0
        for node in range(n):
            if node in visited:
                continue
            num_components += 1
            traverse_component(node)
        
        return num_components
```

## BFS

- deque()の変数名をどうするか迷ったが、探索するnodesということで`nodes_to_explore`としてみた。

```python
from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)

        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
        
        visited = set()
        def traverse_component(node: int) -> None:
            nodes_to_explore = deque([node])
            visited.add(node)
            while nodes_to_explore:
                node = nodes_to_explore.pop()
                for adjacent_node in adjacency_list[node]:
                    if adjacent_node in visited:
                        continue
                    nodes_to_explore.append(adjacent_node)
                    visited.add(adjacent_node)

        num_components = 0
        for node in range(n):
            if node in visited:
                continue
            num_components += 1
            traverse_component(node)
        
        return num_components
```

### UnionFind

- unionfindを使って2つのnodeが同一の親(root)を持っているか判定する。
- Trueだった場合は`num_components = n`から1を引いていく。
- ここの処理の理解に時間がかかったが、すべて連結されてないと仮定し、連結が見つかったらその数を引いていく。

```python
class UnionFind:
    def __init__(self, size: int):
        self.parent = list(i for i in range(size))
        self.rank = [0] * size

    def find(self, node: int) -> int:
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False
            
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else: # elif self.rank[root1] == self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        num_components = n
        for node1, node2 in edges:
            if uf.union(node1, node2):
                num_components -= 1
            
        return num_components
```

## Step3

- visitedの更新を忘れたり、nums_componentsを忘れるミスによるやり直しがあった。
- adjacencyやtraverseの綴は要復習。
- 1回目 7分
- 2回目 9分
- 3回目 8分
