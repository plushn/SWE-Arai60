# 20. Valid Parentheses

## Step1

- Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
- An input string is valid if:
- 1.Open brackets must be closed by the same type of brackets.
- 2.Open brackets must be closed in the correct order.
- 3.Every close bracket has a corresponding open bracket of the same type.

- 最初に提出したときはqueが空の時の処理(閉じるカッコのみの場合)を忘れていた。

```python
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        que = deque()
        for char in list(s):
            if char == '(' or char == '{' or char == '[':
                que.append(char)
            elif char == ')' and len(que) > 0 and que[-1] == '(':
                que.pop()
            elif char == '}' and len(que) > 0 and que[-1] == '{':
                que.pop()
            elif char == ']' and len(que) > 0 and que[-1] == '[':
                que.pop()
            else:
                return False
        if len(que) == 0:
            return True
        else:
            return False
```

## Step2

- 辞書を用いて処理を一般化した。
- else: continue を入れるか省略するか迷いましたが、今回は省略しました。

```python
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        deq = []
        hash_table = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in hash_table:
                deq.append(char)
            elif len(deq) == 0 or hash_table[deq.pop()] != char:
                return False
            #else:
                #continue
        
        if len(deq) == 0:
            return True
        else:
            return False
```

- queの最初に番兵を使ってみる。

```python
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        deq = ["#"]
        hash_table = {'#': '#', '(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in hash_table:
                deq.append(char)
            elif hash_table[deq.pop()] != char:
                return False
                
        if deq.pop() == "#":
            return True
        else:
            return False
```

## Step3

- 翌日以降に解き直す。なんとかできるようになりました。
- 1回目: 8分
- 2回目: 7分
- 3回目: 6分
