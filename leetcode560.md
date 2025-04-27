# 560. Subarray Sum Equals K

## Step1

- `1 <= nums.length <= 2 * 10^4`であり、素直にすべての部分配列の和を求めると、2重ループとなるため時間計算量O(N^2)となるため現実的ではない。
- 1秒間に1000万(10^7)ステップ実行できるとすると、最悪4秒程度かかると推定できる。
- O(N)にする方法が思い浮かばず愚直に解答を作成した。

```python
# TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    result += 1
        return result
```

## Step2

### 累積和(Prefix Sum)

- 累積和を使用してstep1を改良。
- O(N^2)であることには変わらずTLEとなった

```python
# TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i, number in enumerate(nums):
            prefix_sum[i + 1] += prefix_sum[i] + number
        result = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if prefix_sum[j + 1] - prefix_sum[i] == k:
                    result += 1
        return result
```

### 累積和(Prefix Sum) と hashmap を利用した方法

- 時間計算量がstep1の1/2乗に抑えられる。空間計算量はO(1) から O(N)となり悪化したが許容範囲内。
- 累積和のカウントの辞書を作成すればいいことに気づければ、1_two sumのようにhashmapを使っていく。

```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_to_count = defaultdict(int)
        sum_to_count[0] = 1  # a single item is selected from the list
        prefix_sum = 0
        result = 0
        for number in nums:
            prefix_sum += number
            result += sum_to_count[prefix_sum - k]
            sum_to_count[prefix_sum] += 1
        return result
```

## Step3

- 3回解き直す。
- 今回はdefautdictを仕様したが、[get](https://docs.python.org/ja/3/library/stdtypes.html#dict.get)を使用することにより存在しないkeyにアクセスしてKeyErrorになることを防ぐ方法もある。
