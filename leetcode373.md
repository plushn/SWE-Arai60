# 373_FindKPairswithSmallestSums

## Step1

- num1, num2それぞれの和をソートすれば解けるが、二重ループとなるため時間計算量がO(n^2)、ソートがO(n^2 log(n^2))となるので厳しそう。
- とはいってもいい方法を思いつかなかったのでとりあえずやってみたところ、TLEではなくMLEとなった。空間計算量は意識していなかった。
- sum_listの空間計算量がO(n^2)になっていることが原因と考えられる。
- あと、nums1とnum1って誤読しそうかなと思ったので後で変更することにします。

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        sum_list = []
        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                sum_list.append((sum, [num1, num2]))
        sum_list.sort()
        result = [x[1] for x in sum_list]

        return result[:k]
```

- nums1, nums2 ともに昇降順になっているため小さい順に組み合わせればよさそうだが、わからなかったので他の人を参考に。
- heapに追加することは想像できましたが、visitedに追加する処理は自分では思いつきませんでした。

```python
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        sum_and_pairs = []
        visited = set()
        result = []

        heapq.heappush(sum_and_pairs, (nums1[0] + nums2[0], 0, 0))
        while len(result) < k:
            _, nums1_pair, nums2_pair = heapq.heappop(sum_and_pairs)
            result.append([nums1[nums1_pair], nums2[nums2_pair]])

            if nums1_pair + 1 < len(nums1) and (nums1_pair + 1, nums2_pair) not in visited:
                heapq.heappush(
                    sum_and_pairs, 
                    (nums1[nums1_pair + 1] + nums2[nums2_pair], nums1_pair + 1, nums2_pair)
                    )
                visited.add((nums1_pair + 1, nums2_pair))

            if nums2_pair + 1 < len(nums2) and (nums1_pair, nums2_pair + 1) not in visited:
                heapq.heappush(
                    sum_and_pairs, 
                    (nums1[nums1_pair] + nums2[nums2_pair + 1], nums1_pair, nums2_pair + 1)
                    )
                visited.add((nums1_pair, nums2_pair + 1))

        return result
```

## Step2

- エッジケースの対応、重複処理の関数化、変数名の変更を行った。

```python
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 制約上問題ないが、エッジケースに対応
        if not nums1 or not nums2 or k <= 0:
            return []

        # 重複する処理を関数化
        def add_candidates(index_nums1: int, index_nums2:int):
            if index_nums1 < len(nums1) and index_nums2 < len(nums2) and \
                (index_nums1, index_nums2) not in visited:
                heapq.heappush(
                    sum_and_pairs, 
                    (nums1[index_nums1] + nums2[index_nums2], index_nums1, index_nums2)
                    )
                visited.add((index_nums1, index_nums2))
            return

        sum_and_pairs = []
        visited = set()
        result = []

        add_candidates(0, 0)
        while len(result) < k and sum_and_pairs:
            _, index_nums1, index_nums2 = heapq.heappop(sum_and_pairs)
            result.append([nums1[index_nums1], nums2[index_nums2]])
            add_candidates(index_nums1 + 1, index_nums2)
            add_candidates(index_nums1, index_nums2 + 1)

        return result
```

## Step3

- なんとかできるように。変数が多いとそれぞれ何を指しているか混乱しました。わかりやすい変数名が重要ですね。
- 1回目 9分
- 2回目 7分
- 3回目 6分
