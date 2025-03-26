# 347. Top K Frequent Elements

## Step1

- いろいろ調べながら自力で解答しました。
- 辞書の扱い方がまだまだ理解が足りてないのでドキュメントを読みました。
- 考え方としては、各要素の辞書を作成して回数をカウントしていく。そのカウントのヒープを作成して大きい順にk個取り出す。
- heapにタプルとして挿入すると最初の要素でソートされる。heapに挿入できるデータ型はなにか理解していない。そしてどの要素をソートしていくか調べる。

```python
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_count = {}
        results = []

        for num in nums:
            if num in frequent_count:
                frequent_count[num] += 1
            else:
                frequent_count[num] = 1
        
        counter = []
        for key, value in frequent_count.items():
            heapq.heappush(counter, (-value, key))
        
        while len(results) < k:
            temp = heapq.heappop(counter)
            results.append(temp[1])

        return results
```

## Step2

- defaultdictを使用して辞書を初期化することにより存在しないkeyを参照することによるkeyerrorを回避できる。同様にgetメソッドもkeyerrorを回避できる。
- Counterを使えば頻度の辞書を出力してくれる。これ知っていればすぐカウントできたんですね。

```python
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_count = defaultdict(int)
        top_k_nums = []
        result = []

        frequent_count = Counter(nums)        
        for key, value in frequent_count.items():
            heapq.heappush(top_k_nums, (-value, key))        
        while len(result) < k:
            key = heapq.heappop(top_k_nums)[1]
            result.append(key)
        
        return result
```

- heapの代わりにsortを使用してソートしていく。key関数でソートしたい要素を指定できる。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_count = defaultdict(int)
        frequent_count = Counter(nums)
        result = sorted(frequent_count, key=frequent_count.get, reverse=True)  
        return result[:k]
```

- Counterのmost_commonを使えば一発でできるよう

```python
class Solution:
    def topKFrequent(self, nums, k):
        return [num for num, _ in Counter(nums).most_common(k)]
```

## Step3

- 辞書やソートのドキュメントを読みました。
- 実装したことがないものはわかったつもりになりやすいので、次回からは使い慣れていないメソッドや関数を使った解法を試してみたいです。
- 1回目 9分
- 2回目 7分
- 3回目 4分
