# 703. Kth Largest Element in a Stream

- [問題](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

## Step1

- listに毎回val入れてソートする。やはりかなり時間がかかった。init、addの時間計算量はそれぞれsortの O(n logn)となる。
- `1 <= k <= nums.length + 1`であり、__init__ではk = nums.length + 1となる可能性があることに注意。

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.scores = sorted(nums, reverse=1)

    def add(self, val: int) -> int:
        self.scores.append(val)
        self.scores = sorted(self.scores, reverse=1)
        return self.scores[self.k - 1]
```

- heap(優先度付きキュー)を使う。
- heapに追加する際にk番目より大きいscoreを削除するように変更。
- これによりaddの時間計算量はO(logn)となった。
- heapqのドキュメントを読むとheapは二分木であり、heappushとheappopはheapの高さに沿って要素の操作を行うからO(logn)となるよう。

```python
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.scores = nums
        heapq.heapify(self.scores)
        while len(self.scores) > k:
            heappop(self.scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.scores, val)
        if len(self.scores) > self.k:
            heapq.heappop(self.scores)
        return self.scores[0]
```

## Step2

- scoresではk番目までのスコアであることがわからないためtop_k_scoresに変更
- numsが破壊されないようにコピーした。deepcopyだと参照ではなくコピーを生成するらしい。他にいい方法はないだろうか。

```python
import heapq
import copy

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_scores = copy.deepcopy(nums)
        heapq.heapify(self.top_k_scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_scores, val)
        while len(self.top_k_scores) > self.k:
            heapq.heappop(self.top_k_scores)
        
        return self.top_k_scores[0]
```

## Step3

- 何度も書いていくうちにheapの使い方にも慣れてきて、文法ミスも減ってきました。
- 課題:heapを実装してみる。[ドキュメント](https://github.com/python/cpython/blob/3.8/Lib/heapq.py)
- 1回目: 8分
- 2回目: 7分
- 3回目: 3分
