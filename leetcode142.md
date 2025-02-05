# 142. Linked List Cycle II

## Step1

- 141でやったfloydの循環検出法でループを検出するまではできました。ループの開始を探索する方法はよくわからずギブアップしました。

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
```

## Step2

- 解法1 floydの循環検出法
- fastを初期値に移動させて再度追いかける。解説を読んだら納得しましたが、この発想には至らなかったです。

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        # ループが存在せず上のwhileが終了した場合
        if fast.next is None or fast.next.next is None:
            return None
        
        # fastを最初に移動させてもう一度追いかける。
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
```

- 解法2 setを利用
- こちらの方は141の改良であり解答可能であったかなと感じた。

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_node = set()
        node = head

        while node:
            if node in visited_node:
                return node
            visited_node.add(node)
            node = node.next
        return None
```

## Step3

- メモ: クセなのかわかってないのか、ポインターを次に動かさずにループを処理することが多いので気をつける。
- 1回目 5分
- 2回目 3分
- 3回目 2分
