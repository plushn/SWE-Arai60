# 617. Merge Two Binary Trees

## Step1

## 方針

BFSを使ってroot1, root2それぞれのnodeをmergeしていく。  
tree1, tree2のqueueから取り出し、新しいTreeNodeのmerged_treeをqueueに追加していく。  
tree1, tree2のleft, rightをそれぞれmergeし、merged_rootに連結していく。  

## 問題の制約

- nodeの数は2000であるためBFSの時間計算量O(n)で対応できそう。
- `-104 <= Node.val <= 104`

```python
from collections import deque

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        tree1 = deque([root1])
        tree2 = deque([root2])
        merged_root = TreeNode(root1.val + root2.val)
        merged_tree = deque([merged_root])

        while tree1 or tree2:
            node1, node2 = tree1.popleft(), tree2.popleft()
            merged_node = merged_tree.popleft()

            # process left node
            if node1.left is not None and node2.left is not None:
                merged_node.left = TreeNode(node1.left.val + node2.left.val)
                merged_tree.append(merged_node.left)
                tree1.append(node1.left)
                tree2.append(node2.left)
            elif node1.left is not None:
                merged_node.left = node1.left
            elif node2.left is not None:
                merged_node.left = node2.left

            # process right node
            if node1.right is not None and node2.right is not None:
                merged_node.right = TreeNode(node1.right.val + node2.right.val)
                merged_tree.append(merged_node.right)
                tree1.append(node1.right)
                tree2.append(node2.right)
            elif node1.right is not None:
                merged_node.right = node1.right
            elif node2.right is not None:
                merged_node.right = node2.right
            
        return merged_root
```

## Step2

tree1, tree2, merged_treeを一つのqueueから取り出す形に変更し、子のnodeの処理を関数として定義するように変更した。  
最初に書いたコードは子のノードが更新されなかった。[参照](#動かない)

```python
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        merged_root = TreeNode(root1.val + root2.val)
        original_and_merged_node = collections.deque([(root1, root2, merged_root)])

        def merge_nodes(node1, node2):
            if node1 is not None and node2 is not None:
                merged_node = TreeNode(node1.val + node2.val)
                original_and_merged_node.append((node1, node2, merged_node))
                return merged_node
            if node1 is not None and node2 is None:
                return node1
            if node1 is None and node2 is not None:
                return node2
            return None


        while original_and_merged_node:
            node1, node2, merged_node = original_and_merged_node.popleft()
            merged_node.left = merge_nodes(node1.left, node2.left)
            merged_node.right = merge_nodes(node1.right, node2.right)

        return merged_root
```

## Step3

他にも新しくmerged_nodeを作成せずroot1とroot2を破壊的にmergeしていく方法を使っている解法もあった。  
以下に関数が影響を及ぼすスコープを正しく理解せず実装したコードを記載した。

### 動かないコード

`merge_nodes()`の関数に変数に代入しただけだになってしまって、代入した`merged_node.left`や`merged_node.right`が変更されなかったことが原因。
変更した値(`merged_node`)を返すような関数に修正してstep2で実装した。

```python
### 動かない###
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        merged_root = TreeNode(root1.val + root2.val)
        original_and_merged_node = deque([(root1, root2, merged_root)])

        def merge_nodes(node1, node2, merged_node):
            if node1 is not None and node2 is not None:
                merged_node = TreeNode(node1.val + node2.val)   # merged_nodeが関数の外に影響を及ぼしていない。
                original_and_merged_node.append((node1, node2, merged_node))
            if node1 is not None and node2 is None:
                merged_node = node1
            if node1 is None and node2 is not None:
                merged_node = node2


        while original_and_merged_node:
            node1, node2, merged_node = original_and_merged_node.popleft()
            merge_nodes(node1.left, node2.left, merged_node.left)
            merge_nodes(node1.right, node2.right, merged_node.right)

        return merged_root
```
