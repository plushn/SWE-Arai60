# 141_LinkedListCycle

## Step1

- 初見ではそもそもheadの扱い方がわからず手が出ませんでした。Araiさんの動画などを参考にしました。
- 解法1 floydの循環検出法
- 時間計算量O(n)
- 空間計算量O(1) ポインターは2つで定数倍

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        if fast is None or fast.next is None:
            return None

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
```

- 解法2 setを利用
- 時間計算量O(n)
- 空間計算量O(n) setは最悪n個のnodeを格納する必要がある

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited_node = set()
        cur = head
        
        while cur and cur.next:
            if cur in visited_node:
                return True

            visited_node.add(cur)
            cur = cur.next

        return False
```

## Step2

- 解法1 floydの循環検出法

```python
class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slowとfastのポインタの初期化
        slow = head
        fast = head

        # listの中身が0か1のとき
        if fast is None or fast.next is None:
            return None

        # fastがslowに追いつくまでループ
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return None
```

- 解放2 setを利用
- curは対比するものがないためnodeに変更。

```python
class Solution(object):
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_set = set() # 訪れたnodeのset
        node = head
        
        # nodeがsetにあるか確認する
        while node and node.next:
            if node in visited_set:
                return True

            visited_set.add(node)
            node = node.next

        return False
```

## Step3

- 最後の方はほぼ暗記しまったので下記の時間でできるになりましたが、とりあえず自力で書けるようになりました。
- 課題1: PEP8などのコーディング規則はほとんど知らないので次回への課題としたいと思います。
- 課題2: setについて調べる。
- 1回目 10分
- 2回目 4分
- 3回目 3分
- 
