# 206. Reverse Linked List

- [問題](https://leetcode.com/problems/reverse-linked-list/description/)

## Step1

- headが空の場合と要素が1つの場合の処理はできました。
- 繋ぎ変える操作が複雑で混乱してしまい解くことができませんでした。
- current_nodeとnext_nodeの初期化に問題があり、reverseListの最後をNoneにつなぐと考える。
- 繋ぎ変える操作だけでなく、最初と最後がどうなるかも考えると良さそう。

```python
# 初回の回答 失敗
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        current_node = head
        next_node = current_node.next
        
        while next_node:
            dummy_node = next_node.next
            next_node.next = current_node

            current_node = next_node
            next_node = dummy_node
        
        return current_node
```

```python
# 修正後
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # 初期値を修正
        current_node = None
        next_node = head
        
        while next_node:
            dummy_node = next_node.next
            next_node.next = current_node

            current_node = next_node
            next_node = dummy_node
        
        return current_node
```

## Step2

- step1のwhile内を1行に修正。個人的にはstep1が好みです。

```python
# 繋ぎ変える
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        current_node = None
        next_node = head

        while next_node:
            next_node.next, current_node, next_node = current_node, next_node, next_node.next
        
        return current_node
```

- stackを使ってみる
- valを取り出して再度ListNodeに格納していく方法は少々強引な気もしました。

```python
# stack
from collections import deque

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        node = head
        stack = deque()

        result = ListNode()
        result_node = result
        
        while node:
            stack.append(node.val)
            node = node.next
        
        while stack:
            val = stack.pop()
            result_node.val = val
            if stack:
                result_node.next = ListNode()
            result_node = result_node.next
        
        return result
```l

- 再帰
- 再帰は苦手意識がありますが、シンプルでわかりやすい気がします。

```python
# 再帰1 スタックとして取り出す
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        result = self.reverseList(head.next)
        tail = result

        while tail.next:
            tail = tail.next
        tail.next = ListNode(head.val)
        return result
```

```python
# 再帰2 繋ぎ変える
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        result = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return result
```

## Step3

- 今回は色々な方法を試してみたが、最初に書いた繋ぎ変えるのが一番好きでした。
- 解き直しは苦手な再帰で。
- 1回目: 8分
- 2回目: 7分
- 3回目: 4分
