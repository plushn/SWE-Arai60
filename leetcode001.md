# 1. Two Sum

## Step1

- indexの複数形はindexesまたはindices(知らなかった!)。
- indexesは「索引」という意味、indicesは「指数」という意味(今回はこっち)で使われるよう。
- `2 <= nums.length <= 10^4`なので二重ループO(n^2)でも問題なさそうなので素直に解いてみる。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i , j = 0, 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

- 補数の辞書を作成し格納して1重ループに。計算量は以下のようになった。
- 空間計算量が増えたが十分に許容できそう。
- 時間計算量: O(n^2) -> O(n)
- 空間計算量: O(1) -> O(n)

```python
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = defaultdict(int)
        index = 0
        for num in nums:
            complement = target - num
            if complement in num_to_index:
                return [index, num_to_index[complement]]
            num_to_index[num] = index
            index += 1
```

## Step2

- enumerateを使用した。解が存在しない例外にも対応。
- numsが空の場合やtargetが負の場合でも問題なさそう。
- [エラーと例外](https://docs.python.org/dev/tutorial/errors.html)を読みました。

```python
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = defaultdict(int)
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [index, num_to_index[complement]]
            num_to_index[num] = index
        # 制約上問題ないが,解が存在しないとき
        raise ValueError
```

## Step3

- 翌日以降に解き直し。
- 1回目 6分
- 2回目 3分
- 3回目 3分
