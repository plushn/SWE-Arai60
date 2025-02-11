# 083_RemoveDuplicatesfromSortedList.md

## Step1

- 答えを見ればコードをかけそうだなと思いましたが、listを繋ぎ変える操作が難しく解けませんでした。

## Step2

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        cur_node = head
        nxt_node = cur_node.next

        while nxt_node:
            if cur_node.val == nxt_node.val:
                cur_node.next = cur_node.next.next
                nxt_node = cur_node.next
            else:
                cur_node = cur_node.next
                nxt_node = cur_node.next
        return head
```

## Step3

- 時間の余裕ができてきたのでもう少し簡略化して解くペース上げていきたいです。
- 1回目 7分
- 2回目 3分
- 3回目 2分
