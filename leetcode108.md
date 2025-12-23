# 108. Convert Sorted Array to Binary Search Tree

## Step1

## 方針

`hight-balanced binary searcj tree` が少しわかりにくかったが、|左の高さ - 右の高さ| <= 1を満たしていくには、配列の中点でtreeを作っていきそれを繋いでいけばいい。  
numsは昇降順であるためその中点をrootとしてtreeを作成していけばよさそう。  
中点の左右で分離してその中点で再帰的にtreeをつなげていく。

## 問題の制約

時間計算量O(n)、空間計算量(log n)

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)

            return root

        return build_tree(0, len(nums) - 1)
```

## Step2

queueを使って実装してみた。コードが長くなり、左右の範囲をqueueに追加しているため読みづらさがあるかと思いました。  
再帰で実装した方が直感的でシンプルですね。

```python
import collections

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(parent, start, end, direction):
            if start > end:
                return None
            mid = (start + end) // 2
            child = TreeNode(nums[mid])
            if direction == "left":
                parent.left = child
            else:
                parent.right = child
            return child, (start, mid - 1), (mid + 1, end)

        if not nums:
            return None

        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])
        parent_and_child = collections.deque([(root, (0, mid - 1), (mid + 1, len(nums) - 1))])

        while parent_and_child:
            parent, left_range, right_range = parent_and_child.popleft()
            l_start, l_end = left_range
            r_start, r_end = right_range

            left_node = build_tree(parent, l_start, l_end, "left")
            if left_node is not None:
                parent_and_child.append(left_node)
            right_node = build_tree(parent, r_start, r_end, "right")
            if right_node is not None:
                parent_and_child.append(right_node)
        
        return root
```

## Step3

再帰を使って3度実装した。
以下はほぼ変わらないと思いますが、載せておきます。

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(val=nums[mid])

            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)
            
            return node
        
        return build_tree(0, len(nums) - 1)
```
