# 112. Path Sum

## Step1

DFSやBFSで各nodeの値を足していって葉の場合にtargetSumと一緒となるか判定すればよさそう。10分くらいで解答できた。

## 方針

rootからleafまでの経路の経路を探索し、その値の合計が目標値と等しいかどうかを探索する。  
nodeとそれまでの合計値を保持し、DFS/BFSで探索していく。

## 問題の制約

The number of nodes in the tree is in the range [0, 5000].

- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000


## Step2

### stackを使って実装

葉までの合計値を加算していったが、他にはtargetSumから減算していく方法もあった。本問題ではどちらでも変わらなそうかな。  
https://github.com/5ky7/arai60/pull/26/files#diff-0c860cd754249868513e4f9054206317fa33d0f548fc3896ac2b3e11822fd852

時間計算量: O(n)
空間計算量: O(h)
n:nodeの数 h: treeの高さ

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        frontiers = collections.deque([(root, root.val)])   # (node, total)

        while frontiers:
            node, total = frontiers.pop()

            if node.left is None and node.right is None and targetSum == total:
                return True
            if node.left is not None:
                frontiers.append((node.left, total + node.left.val))
            if node.right is not None:
                frontiers.append((node.right, total + node.right.val))

        return False
```

### 再帰での実装

targetSumからnode.valを引いていき、葉にたどり着いたとき、0となっているかどうかを返す。  
そうでない場合は、その左右の子がTrueかFalseかどうかを再帰で判定していく。
今回は減算で実装した。

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val

        if root.left is None and root.right is None:
            return targetSum == 0
        
        return (
            self.hasPathSum(root.left, targetSum)
            or self.hasPathSum(root.right, targetSum)
        )
```

## Step3
