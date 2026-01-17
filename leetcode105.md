# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Step1

inorder,preorderという用語がわからなかった。[参考](https://engineer.yeele.net/algorithm/data-structure/binary-tree-traversal/)

- preorder (先行順巡回 / 前順): 現在のnodeを最初(Pre)に処理する。(根 → 左 → 右)
- inorder (中間順巡回 / 中順): 現在のnodeを中間(In)に処理する。(左 → 根 → 右)
- postorder (後行順巡回 / 後順): 現在のnodeを最後(Post)に処理する。(左 → 右 → 根)

grobalとnonlocalの違いを復讐

- [global](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement): glebalスコープを操作する場合
- [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement): 親関数のスコープを操作する場合
- [Python のスコープと名前空間](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)

## 方針

自力では解けなさそうだったのでgeminiと一緒に考える。  
preorderで次のrootを取得し、inorderでその左右のnodeを取得するしていけば良い。  
preorderのrootがinorderでindexを探すための辞書を作成する。

## 問題の制約

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

```python
from typing import Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_to_index = {val : i for i, val in enumerate(inorder)}
        preorder_index = 0

        def build_subtree(left: int, right: int) -> Optional:
            nonlocal preorder_index

            root_val = preorder[preorder_index]
            root = TreeNode(val=root_val)
            preorder_index += 1

            mid = inorder_to_index[root_val]

            if left < mid:
                root.left = build_subtree(left, mid - 1)
            if mid < right:
                root.right = build_subtree(mid + 1, right)
            return root
        
        return build_subtree(0, len(inorder) - 1)
```

## Step2

### スタック+iterartor

スタックで実装する場合は、rightー>leftの順に積んでいかなければいけないことに注意する。

```python
from typing import Optional, List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_to_index = {val: i for i, val in enumerate(inorder)}
        preorder_iter = iter(preorder)
        root = TreeNode()
        frontiers = [(root, 0, len(inorder) - 1)]  # (node, left, right)
        
        while frontiers:
            node, left, right = frontiers.pop()
            node_val = next(preorder_iter)
            inorder_index = inorder_to_index[node_val]
            node.val = node_val
            if inorder_index < right:
                node.right = TreeNode()
                frontiers.append((node.right, inorder_index + 1, right))
            if left < inorder_index:
                node.left = TreeNode()
                frontiers.append((node.left, left, inorder_index - 1))
                
        return root
```

### 再帰+iteraror

```python
from typing import Optional, List

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        inorder_to_index = {val: i for i, val in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def build_subtree(left: int, right: int) -> TreeNode:
            root_val = next(preorder_iter)
            root = TreeNode(root_val)

            mid = inorder_to_index[root_val]

            if left < mid:
                root.left = build_subtree(left, mid - 1)
            if mid < right:
                root.right = build_subtree(mid + 1, right)
            
            return root

        return build_subtree(0, len(inorder) - 1)
```

## Step3
