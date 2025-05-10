# 349. Intersection of Two Arrays

## Step1

- setを使って積集合を求めるだけでできそう。ACだけなら簡単にできそう。
- [set](https://docs.python.org/ja/3/library/stdtypes.html#set-types-set-frozenset)の使い方が未熟なので読む。
- &ではなく、[intersection](https://docs.python.org/ja/3.13/library/stdtypes.html#frozenset.intersection)でも可能。

```python
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        unique_nums1 = set(nums1)
        unique_nums2 = set(nums2)
        return list(unique_nums1 & unique_nums2)
```

## Step2

### 解法1 積集合: 最初の解答を改良

- 二つのlistの長さに大きな差がある場合、短い方のlistの要素数Nとすると時間計算量がO(N)となる。

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            raise ValueError("nums1 or nums2 is empty")
        if not all(isinstance(x, int) for x in nums1):
            raise TypeError("nums1 includes non-numeric values")
        if not all(isinstance(x, int) for x in nums2):
            raise TypeError("nums2 includes non-numeric values")
        
        unique_num = []
        if len(nums1) > len(nums2):
            long, short = set(nums1), set(nums2)
        else:
            long, short = set(nums2), set(nums1)
        for number in short:
            if number in long:
                unique_num.append(number)
        return unique_num
```

### 解法2 two pointer

- それぞれのlistをsortし、それぞれのpointerを比較していく。
- 時間計算量はそれぞれソートするためO(N logN + M logM)となるが、入力されるlistがソートされている場合はO(N + M)となる。(N, Mはそれぞれnums1, nums2の長さ)

```python
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        group1 = sorted(nums1)
        group2 = sorted(nums2)
        index1, index2 = 0, 0
        unique_nums = []

        while index1 < len(group1) and index2 < len(group2):
            if group1[index1] < group2[index2]:
                index1 += 1
                continue
            if group1[index1] > group2[index2]:
                index2 += 1
                continue
            unique = group1[index1]
            unique_nums.append(unique)
            while index1 < len(group1) and group1[index1] == unique:
                index1 += 1
            while index2 < len(group2) and group2[index2] == unique:
                index2 += 1
        return unique_nums
```

## Step3

- 最初に思いついた解答ではタイピング練習になりそうなので、two pointerで3回解いてみる。
- 他にも二分探索やマージソートで解答している方もいるので時間がある時に取り組みたい。
- 1回目 7分
- 2回目 5分
- 3回目 5分
