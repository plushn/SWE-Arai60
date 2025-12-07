# 104. Maximum Depth of Binary Tree

## Step1

(node, depth) をタプルをDFSやBFSで捜査していけば解けそう。細かいミスもあったが10分程度で完成。

```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        nodes_and_depth = deque([(root, 1)]) # (node, depth)
        max_depth = 1

        while nodes_and_depth:
            node, depth = nodes_and_depth.popleft()
            max_depth = max(max_depth, depth)

            if node.left:
                nodes_and_depth.append((node.left, depth + 1))
            if node.right:
                nodes_and_depth.append((node.right, depth + 1))
        return max_depth
```

## Step2

- 最悪時間計算量:O(n)
- 最悪空間計算量:O(n)
n: rootの要素数

- BFS (Queue):
  - `deque` を使用。
  - `for _ in range(len(queue))` の構文を使うことで、level（階層）ごとの処理できる。
- DFS (Recursion):
  - コードがシンプル。
  - Pythonでは再帰の深さ制限に注意が必要。

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        max_depth = 1
        node_and_depth = deque([(root, 1)])

        while node_and_depth:
            node, depth = node_and_depth.popleft()
            max_depth = max(depth, max_depth)

            if node.left:
                node_and_depth.append((node.left, depth + 1))
            if node.right:
                node_and_depth.append((node.right, depth + 1))
        
        return max_depth
```

## Step3

- 1回目 6分
- 2回目 5分
- 3回目 3分

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        node_and_level = deque([(root, 1)])  # (node, level)
        max_level = 1

        while node_and_level:
            node, level = node_and_level.popleft()
            if node.right:
                node_and_level.append([node.right, level + 1])
            if node.left:
                node_and_level.append([node.left, level + 1])
            max_level = max(max_level, level)
        return max_level
```

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        nodes_and_depth = deque([root])
        depth = 0

        while nodes_and_depth:
            depth += 1
            for _ in range(len(nodes_and_depth)):
                node = nodes_and_depth.popleft()

                if node.left:
                    nodes_and_depth.append(node.left)
                if node.right:
                    nodes_and_depth.append(node.right)

        return depth
```

```python
# 再帰で実装

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return max(depth_left, depth_right) + 1
```
