# 82. Remove Duplicates from Sorted List II

## Step1

- 3連続のpointerを比較するところまでは思いついたが、最初に同じ値が出現するときの処理ができなかった。
- 新たにListNodeを作成し、その先頭にノードを追加する。先頭はNone以外でもよさそうだが、他の数字にするメリットも思いつかないのでNoneとして処理していく。

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        pointer = dummy_head

        while pointer.next and pointer.next.next:
            if pointer.next.val == pointer.next.next.val:
                node = pointer.next
                while node.next and node.val == node.next.val:
                    node.next = node.next.next
                pointer.next = node.next
            else:
                pointer = pointer.next
        
        return dummy_head.next
```

## Step2

- dummy_nodeを作成する時に引数に入れて変更。
- pointer.next と pointer.next.next をそれぞれ current_node と next_node に変更。

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node
        dummy_node = ListNode(None, head)
        pointer = dummy_node

        # move pointer to the next node
        while pointer.next and pointer.next.next:
            current_node = pointer.next
            next_node = current_node.next
            if current_node.val == next_node.val:
                # skip duplicate nodes
                while next_node and current_node.val == next_node.val:
                    next_node = next_node.next
                pointer.next = next_node
            else:
                pointer = pointer.next

        return dummy_node.next
```

## Step3

- 反省:dummy_nodeを作成することができなかったが、やっていることは基本的に83を発展させたものであると感じました。明日以降もう一度解き直したいです。
- 1回目 9分
- 2回目 7分
- 3回目 5分
