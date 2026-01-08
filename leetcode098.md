# 98. Validate Binary Search Tree

## Step1

## 問題の制約

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

## 方針

subtreeの判定を正しく処理できなかった。
これは下記のような場合、上位levelの最大、最小値を保持していないため10 < 6となることが原因であった。
```
      10
     /  \
    5    15
        /  \
       6   20
```

```python
# not accepted
# step3 で修正版を作成した
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        frontier = deque([root])

        while frontier:
            level_size = len(frontier)
            
            for _ in range(level_size):
                node = frontier.popleft()
                if node.left and not (node.left.val < node.val):
                    return False
                if node.right and not (node.val < node.right.val):
                    return False
        return True
```

## Step2

### 再帰

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node: Optional[TreeNode], low: int, high: int) -> bool:
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return (is_valid(node.left, low, node.val)
                    and is_valid(node.right, node.val, high))

        return is_valid(root, -math.inf, math.inf)
```

### Generator + 再帰

- ジェネレーター[yield](https://docs.python.org/3.14/reference/expressions.html#yield-expressions)をあまり理解していなかったので復習。
- ジェネレーターの委譲[yield form](https://docs.python.org/3.14/whatsnew/3.3.html#pep-380)

この方法だと`yield node`の位置を変えるだけでpreorder、postorderに変更でき使いやすそう

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def generate_inorder(node):
            if node.left is not None:
                yield from generate_inorder(node.left)
            yield node
            if node.right is not None:
                yield from generate_inorder(node.right)

        for previous, current in itertools.pairwise(generate_inorder(root)):
            if current.val <= previous.val:
                return False

        return True
```

## Step3

step1の大小評価を修正し、node、最大値、最小値を保持するようにした。

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        nodes_in_current_level = deque([(root, -math.inf, math.inf)]) # (node, minimum limit, maximum limit)
        while nodes_in_current_level:
            node, low, high = nodes_in_current_level.popleft()

            if not (low < node.val < high):
                return False
            if node.left is not None:
                nodes_in_current_level.append((node.left, low, node.val))
            if node.right is not None:
                nodes_in_current_level.append((node.right, node.val, high))

        return True
```
