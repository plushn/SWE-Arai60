# 102. Binary Tree Level Order Traversal

## Step1

- BFSでいけそう。最初、node.valを格納せずnodeを格納してしまったため時間がかかったが、15分以内で自力でaccept。

## 方針

levelごとのlistを作成するため、BFSでtreeをlevelごとに走査していく。

## 問題の制約

- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_in_level = [root]
        values = []

        if root is None:
            return values
            
        while nodes_in_level:
            nodes_in_next_level = []
            values_in_level = []

            for node in nodes_in_level:
                if node is None:
                    continue
                values_in_level.append(node.val)
                if node.left:
                    nodes_in_next_level.append(node.left)
                if node.right:
                    nodes_in_next_level.append(node.right)

            nodes_in_level = nodes_in_next_level
            values.append(values_in_level)
        return values
```

## Step2

時間計算量: O(n)
空間計算量: O(n)

level内の操作を関数を使ってみたが、next_levelの処理と、current_valuesの処理を同時にやっており、かえってわかりにくくなったように感じる。
while内のnodes_in_levelとvalues_in_levelのlevelが対応しなくなるのも原因か。
無理やり関数を使わない方がわかりやすい気もする。

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_in_level = [root]
        levels = []

        if root is None:
            return levels

        def get_next_nodes_and_current_val(current_nodes):
            next_nodes = []
            current_values = []
            for node in current_nodes:
                current_values.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            return next_nodes, current_values

        while nodes_in_level:
            nodes_in_level, values_in_level = get_next_nodes_and_current_val(nodes_in_level)
            levels.append(values_in_level)
            
        return levels
```

## Step3

step1とほぼ同じようになったが3回繰り返す。

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_in_level = [root]
        levels = []

        if root is None:
            return levels
        
        while nodes_in_level:
            next_level = []
            values_in_level = [0] * len(nodes_in_level)

            for i, node in enumerate(nodes_in_level):
                if node is not None:
                    values_in_level[i] = node.val
                
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            
            nodes_in_level = next_level
            levels.append(values_in_level)
        
        return levels
```
