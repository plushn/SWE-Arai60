# 103. Binary Tree Zigzag Level Order Traversal

## Step1

102と同様にBFSでいけそう。listへの追加方向を変更していくように変更した。

## 方針

102の実装をis_reverseddでリストへの挿入方向をしていするように変更した。

## 問題の制約

- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        nodes_in_level = deque([root])
        zigzag_levels = []
        is_reversed = True
            
        while nodes_in_level:
            level_size = len(nodes_in_level)
            values_in_level = [0] * level_size

            for i in range(level_size):
                node = nodes_in_level.popleft()
                
                if is_reversed:
                    values_in_level[i] = node.val
                else:
                    values_in_level[level_size - i - 1] = node.val

                if node.left:
                    nodes_in_level.append(node.left)
                if node.right:
                    nodes_in_level.append(node.right)

            zigzag_levels.append(values_in_level)
            is_reversed = not is_reversed
        return zigzag_levels
```

## Step2

関数でlevel内の操作をまとめてみた。
`is_reversed`はどちらが順行方向かわかりにくいと思い`is_left_to_right`にして明示的に変更した。  
(まあ、組み込み関数の`sort()`でも昇順、降順ではなくreverseを使っているので考えすぎな気もしますが)

- 時間計算量: O(n)
- 空間計算量: O(n)

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        nodes_in_level = [root]
        levels = []
        is_left_to_right = True

        def process_level(current_level, is_left_to_right):
            level_size = len(current_level)
            next_level = []
            current_values = [0] * level_size

            for i, node in enumerate(current_level):
                if is_left_to_right:
                    current_values[i] = node.val
                else:
                    current_values[level_size - i - 1] = node.val

                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            return next_level, current_values
            
        while nodes_in_level:
            nodes_in_level, current_values = process_level(nodes_in_level, is_left_to_right)
            levels.append(current_values)
            is_left_to_right = not is_left_to_right

        return levels
```

## Step3

step1とほぼ同じようになったが3回繰り返す。

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_in_level = [root]
        zigzag_levels = []
        is_left_to_right = True

        if root is None:
            return zigzag_levels
        
        while nodes_in_level:
            next_level = []
            level_size = len(nodes_in_level)
            values_in_level = [0] * level_size

            for i, node in enumerate(nodes_in_level):
                if node is not None:
                    if is_left_to_right:
                        values_in_level[i] = node.val
                    else:
                        values_in_level[level_size - i - 1] = node.val
                
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            
            nodes_in_level = next_level
            zigzag_levels.append(values_in_level)
            is_left_to_right = not is_left_to_right
        
        return zigzag_levels
```
