# 387. First Unique Character in a String

## Step1

- 自分の良くない癖なのだが、すぐに解けない問題をあきらめられず40分かけて解いてしまった。スマートではないがacceptedされた。
- 文字列のindexのhashmapを作成し、2回目以降であればindex = len(s) + 1とする。その辞書で最小のindexを探す方法。
- step2で改良しましたが、strすべての文字のindexの対応する辞書ってenumerateで数え上げるのと同じなんであまり意味のないことしてましたね。。。

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        word_to_index = {}
        duplicated = set()
        for i, word in enumerate(s):
            if word not in word_to_index.keys():
                word_to_index[word] = i
            else:
                word_to_index[word] = len(s) + 1  # indexの外へ。下でmin_indexで最小値を比較するため。
                duplicated.add(word)
        min_index = len(s) + 1
        for word, index in word_to_index.items():
            if index not in duplicated:
                min_index = min(min_index, index)
        if min_index > len(s):
            min_index = -1
        return min_index
```

## Step2

- いずれの方法も時間計算量O(N)、最悪の空間計算量O(N)となるが、可読性が高いdefautdictやCounterを使うのが好み。

### step1改良

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique_to_index = {}
        seen = set()
        for index, word in enumerate(s):
            if word in unique_to_index.keys():
                seen.add(word)
                del unique_to_index[word]
                continue
            if word in seen:
                continue
            unique_to_index[word] = index
        if not unique_to_index:
            return -1
        return min(unique_to_index.values())
```

### 辞書

- 辞書は格納順になっているため、初めてcountが1となる場合を探すだけで良かった。

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_index = defaultdict(int)
        for word in s:
            char_to_index[word] += 1
        for index, word in enumerate(s):
            if char_to_index[word] == 1:
                return index
        return -1
```

### Counter

- [Counter](https://github.com/python/cpython/blob/3.13/Lib/collections/__init__.py#L548)の内部実装を確認。cpythonも少しずつ読んでいきたい。

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = Counter(s)
        for index, word in enumerate(s):
            if char_to_count[word] == 1:
                return index
        return -1
```

## Step3

- それぞれ違った実装を試してみた。
- 他にもLRUによる解法もあるみたいなのでまた取り組みたい。
