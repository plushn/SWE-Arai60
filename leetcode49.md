# 49. Group Anagrams

## Step1

- 文字頻度の辞書を作成すればできそうと思い、`Counter()`を使って文字をカウントすればいいと思ったが、そこからどう処理すればいいかわからずギブアップ。
- 文字列をソートし、それをkeyとして辞書に追加していく。文字列をキーとした辞書を作る発想に至れば解答できそうと感じた。

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_to_groups = defaultdict(list)
        for str in strs:
            sorted_strs = "".join(sorted(str))
            sorted_to_groups[sorted_strs].append(str)
        
        result = []
        for str_group in sorted_to_groups.values():
            result.append(str_group)

        return result
```

## Step2

- 例外処理を実装。
- all()はiterableを引数に必要がある。
- 辞書のitems(),keys(),values()は[辞書ビューオブジェクト](https://docs.python.org/ja/3/library/stdtypes.html#dict-views)を返す。それをlistに変換するだけてで解答可能。

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 制約上問題ないが、小文字以外をエラーで返す
        if not all(s.islower() for s in strs if s):
            raise ValueError("strs consists of only lowercase letters.") 

        sorted_to_groups = defaultdict(list)
        for str in strs:
            sorted_strs = "".join(sorted(str))
            sorted_to_groups[sorted_strs].append(str)

        return list(sorted_to_groups.values())
```

- 最初に思いついた文字頻度の辞書での解法を考えてみる。
- すべての文字の辞書を作成し、それにタプルに変換すれば使える。
- タプル知識不足があった。リストや辞書をタプルを使ってiterableに変換し辞書のkeyとして利用できるようになる。
- `ord(char) - ord('a')`を使うことによりunicodeのaから何番目のindexかを返す。

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        counts_to_groups = defaultdict(list)
        for str in strs:
            alphabet_counter = [0] * 26
            for char in str:
                alphabet_counter[ord(char) - ord('a')] += 1
            counts_to_groups[tuple(alphabet_counter)].append(str)
        
        return list(counts_to_groups.values())
```

## Step3

- 課題: 下記のドキュメントを読んだ。特にiterableはまだまだ理解が足りず、今までデータ型について深く考えていなかったので、これから意識して調べていく必要がある。
  - [iterable](https://docs.python.org/3/glossary.html#term-iterable)
  - [all()](https://docs.python.org/3/library/functions.html#all)
  - [ord()](https://docs.python.org/3/library/functions.html#ord)
- 1回目 6分
- 2回目 4分
- 3回目 4分
