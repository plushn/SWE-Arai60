# 111. Minimum Depth of Binary Tree

## Step1

方針としては、104. Maximum Depth of Binary Treeと同様にDFSやBFSでtreeを走査し、終端に到達したらdepthを更新すればできそう。  
max_depthを更新していくようにmin_depthを更新していくように作成。

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        nodes_and_depth = deque([(root, 1)]) # (node, depth)
        min_depth = 10 ** 5 + 1

        while nodes_and_depth:
            node, depth = nodes_and_depth.popleft()

            if node.left:
                nodes_and_depth.append((node.left, depth + 1))
            if node.right:
                nodes_and_depth.append((node.right, depth + 1))
            
            if node.right is None and node.left is None:
                min_depth = min(min_depth, depth)
        return min_depth
```

## Step2

全探索せずにBFSでlevelを走査し、葉のノードを見つけたらreturnするように改良した。

- 時間計算量: O(n)
- 空間計算量: O(n)

```python
import collections

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        nodes_in_level = collections.deque([root])

        while nodes_in_level:
            depth += 1
            n = len(nodes_in_level)
            for _ in range(n):
                node = nodes_in_level.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    nodes_in_level.append(node.left)
                if node.right:
                    nodes_in_level.append(node.right)
```

## Step3

BFS、DFSでそれぞれ実装した。

```python
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        nodes_in_level = deque([root])

        while nodes_in_level:
            depth += 1
            for _ in range(len(nodes_in_level)):
                node = nodes_in_level.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    nodes_in_level.append(node.left)
                if node.right:
                    nodes_in_level.append(node.right)
```

特にメリットは無さそうですが、個人的にはdepthを最初に更新する方が好みでした。

```python
from collections import deque

class Solution:クラス 解決策:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        nodes_in_levels = deque([root])

        while nodes_in_levels:
            n = len(nodes_in_levels)
            for _ in range(n):
                node = nodes_in_levels.popleft()
                if not node.right and not node.left:
                    return depth
                
                if node.right:
                    nodes_in_levels.append(node.right)
                if node.left:
                    nodes_in_levels.append(node.left)
            depth += 1
```

```python
# 再帰DFS

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def traverse_nodes(node):
            if not node:
                return 0
            if not node.left:
                return traverse_nodes(node.right) + 1
            if not node.right:
                return traverse_nodes(node.left) + 1
            
            return min(traverse_nodes(node.left), traverse_nodes(node.right)) + 1
        return traverse_nodes(root)
```
