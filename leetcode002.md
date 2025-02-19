# 2. Add Two Numbers

## Step1

- l1, l2の要素数が異なる場合の処理ができれば比較的手が出そうかなと思いました。
- 最初の解答はListNodeのvalメソッドは値を返すだけで書き換えれるわけではないからエラーが発生した?

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        res = dummy_node
        dummy_digit = 0

        while l1 or l2:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0
            sum_digit = val_l1 + val_l2 + dummy_digit
            res.val = sum_digit % 10
            res = res.next
            dummy_digit = sum_digit // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if dummy_digit > 0:
            res.val = 1
        
        return dummy_node.next
```

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        res = dummy_node
        dummy_digit = 0

        while l1 or l2:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0
            sum_digit = val_l1 + val_l2 + dummy_digit
            res.next = ListNode(sum_digit % 10)
            dummy_digit = sum_digit // 10

            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if dummy_digit > 0:
            res.next = ListNode(dummy_digit)
        return dummy_node.next
```

## Step2

- carry_digitをwhileループの中に入れるように変更した。コード自体は短くなったが、Runtimeは長くなった(条件分岐が多くなったことが原因か?)

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        result = dummy_node
        carry_digit = 0

        while l1 or l2 or carry_digit:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0
            sum_digit = val_l1 + val_l2 + carry_digit
            result.next = ListNode(sum_digit % 10)
            carry_digit = sum_digit // 10

            result = result.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_node.next
```

## Step3

- 解いた翌日以降に解き直してみたが、解けるようになっていた。
- 1回目 7分
- 2回目 5分
- 3回目 5分
