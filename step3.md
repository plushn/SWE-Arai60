```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for num1, num2 in edges:
            adjacency_list[num1].append(num2)
            adjacency_list[num2].append(num1)
        
        visited = set()
        def traverse_component(node: int) -> None:
            if node in visited:
                return 
            visited.add(node)
            for neighbor in adjacency_list[node]:
                traverse_component(neighbor)
        
        num_components = 0
        for node in range(n):
            if node in visited:
                continue
            num_components += 1
            traverse_component(node)

        return num_components
```

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_nodes = defaultdict(list)
        for node1, node2 in edges:
            adjacency_nodes[node1].append(node2)
            adjacency_nodes[node2].append(node1)
        
        visited = set()
        def traverse(node: int) -> None:
            if node in visited:
                return 
            to_explore = deque([node])
            while to_explore:
                node1 = to_explore.popleft()
                if node1 in visited:
                    continue
                visited.add(node1)
                for node2 in adjacency_nodes[node1]:
                    to_explore.append(node2)
        
        num_components = 0
        for node in range(n):
            if node in visited:
                continue
            num_components += 1
            traverse(node)
        return num_components
```

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_nodes = defaultdict(list)
        for node1, node2 in edges:
            adjacency_nodes[node1].append(node2)
            adjacency_nodes[node2].append(node1)
        
        visited = set()
        def traverse(node: int) -> None:
            if node in visited:
                return
            to_explore = deque([node])
            while to_explore:
                node = to_explore.pop()
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in adjacency_nodes[node]:
                    to_explore.append(neighbor)
        
        num_components = 0
        for node in range(n):
            if node in visited:
                continue
            num_components += 1
            traverse(node)
        return num_components

```
