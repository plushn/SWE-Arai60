# 083_RemoveDuplicatesfromSortedList.md

## Step1

- 答えを見ればコードをかけそうだなと思いましたが、listを繋ぎ変える操作が難しく解けませんでした。

## Step2

- 連続する2つのポインターを用意して比較する。
  
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

- 他の解答では、上の解答のwhileの条件に同値かどうか比較していた。
- nxt_node = cur_node.next がなくなるため if head is None の処理が不要になる。(head=NoneだとNone.nextがAtributeErrorになる)

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node:
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            node = node.next

        return head
```

## Step3

- 課題: 時間をおいて再度解き直してみる。
- 時間の余裕ができてきたのでもう少し解くペース上げていきたいです。
- 1回目 7分
- 2回目 3分
- 3回目 2分
