# 127. Word Ladder

## Step1

BFSでwordListを探索していく感じかなと思いながら5分経過し他の回答を参考にした。  
最初問題文を理解できていなかったが、「移動した回数」ではなく、「シーケンス（経路）に含まれる単語の数」(' the number of words in the shortest transformation sequence')であるため、'endWord == beginWord'の場合でも1となる。  
今までは関数名がキャメルケースであり、統一性を持たせるためにキャメルケースを使用してみたが、変数名をスネークケースで書く習慣がついたためか、かなり違和感があったのでstep2以降ではスネークケースに戻した。  
wordListをsetにしないとTLEになってしまう。[時間計算量](https://wiki.python.org/moin/TimeComplexity)  

- listの場合O(n)となるが、setの場合は平均O(1)となる。
- 時間計算量は、setの場合O(N L)、listの場合、O(N^2 L)となる。
- (N: wordList.length <= 5000, L: beginWord.length <= 10)

```python
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char == word[i]:
                        continue

                    nextWord = list(word)
                    nextWord[i] = char
                    nextWordStr = "".join(nextWord)

                    if nextWordStr in wordSet and nextWordStr not in visited:
                        visited.add(nextWordStr)
                        queue.append((nextWordStr, steps + 1))
        return 0
```

## Step2

### BFS

[ascii_lowercase](https://docs.python.org/ja/3/library/string.html#string.ascii_lowercase)でa~zを処理する。
[ordやchr](https://docs.python.org/ja/3.13/library/functions.html#ord)の使い方を復習。step3で使用してみた。
時間計算量:O(n m^2) 空間計算量:O(n)  n:単語の要素数 m:wordの最大length

```python
from collections import deque
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        word_used = set([beginWord])
        word_candidates = deque([(beginWord, 1)]) # (word, step)

        if endWord not in word_set:
            return 0

        while word_candidates:
            current_word, current_step = word_candidates.popleft()

            if current_word == endWord:
                return current_step
            
            for i in range(len(current_word)):
                for char in ascii_lowercase:
                    if char == current_word[i]:
                        continue
                    
                    # prosess next word
                    word_processed = list(current_word)
                    word_processed[i] = char
                    next_word = "".join(word_processed)
                    next_step = current_step + 1

                    if next_word in word_set and next_word not in word_used:
                        word_candidates.append((next_word, next_step))
                        word_used.add(next_word)
        
        return 0
```

### hash mapとBFSを使って高速化

全ての単語についてワイルドカード * を含んだパターンを作ったもののリストを作成。
'hot' の隣接単語の場合、hot -> *ot -> [hot, aot, bot]

```python
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        pattern_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_dict[pattern].append(word)

        word_and_step = deque([(beginWord, 1)])
        word_used = {beginWord}

        while word_and_step:
            current_word, steps = word_and_step.popleft()
            
            if current_word == endWord:
                return steps
            
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i + 1:]
                
                for neighbor in pattern_dict[pattern]:
                    if neighbor not in word_used:
                        word_used.add(neighbor)
                        word_and_step.append((neighbor, steps + 1))
                
        return 0
```

### 双方向BFS

始点と終点の両端から同時にBFSを行い、中間で出会った時点で最短経路を確定させる

```python
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0
        
        front_layer = {beginWord}
        back_layer = {endWord}
        
        step = 1
        
        if beginWord in word_set:
            word_set.remove(beginWord)
            
        while front_layer and back_layer:
            if len(front_layer) > len(back_layer):
                front_layer, back_layer = back_layer, front_layer
            
            new_layer = set()
            
            for word in front_layer:
                for i in range(len(word)):
                    for char in ascii_lowercase:
                        if char == word[i]:
                            continue
                            
                        next_word = word[:i] + char + word[i+1:]
                        
                        if next_word in back_layer:
                            return step + 1
                        
                        if next_word in word_set:
                            new_layer.add(next_word)
                            word_set.remove(next_word)
            
            front_layer = new_layer
            step += 1
            
        return 0
```

## Step3

ミスした箇所

- キャメルケースとスネークケースが混ざってしまうことがあった。
- popleft() -> leftpop()にしてしまった。
- setに追加を忘れている。追加するものが間違っている。
- range(ord("a"), ord("z"))としてしまい、zまで範囲が及んでいなかった。

時間

- 1回目 12分
- 2回目 9分
- 3回目 8分

```python
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        candidates = deque([(beginWord, 1)])
        word_used = set()

        while candidates:
            word, step = candidates.popleft()
            if word == endWord:
                return step

            for i in range(len(word)):    
                for char_code in range(ord("a"), ord("z") + 1):
                    char = chr(char_code)
                    if char == word[i]:
                        continue

                    transformed_processed = list(word)
                    transformed_processed[i] = char
                    transformed = "".join(transformed_processed)

                    if transformed not in word_set:
                        continue
                    if transformed in word_used:
                        continue

                    word_used.add(transformed)
                    candidates.append((transformed, step + 1))
        return 0
```

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        candidates = deque([(beginWord, 1)])
        usedWords = set()

        while candidates:
            word, step = candidates.popleft()
            if word == endWord:
                return step

            for i in range(len(word)):
                for char in "qwertyuiopasdfghjklzxcvbnm":
                    if char == word[i]:
                        continue
                    
                    transformed = word[:i] + char + word[i + 1:]

                    if transformed not in wordSet or transformed in usedWords:
                        continue
                    usedWords.add(transformed)
                    candidates.append((transformed, step + 1))
        return 0
```

```python
from collections import deque
from string import ascii_lowercase 


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        word_used = set(beginWord)
        word_candidates = deque([(beginWord, 1)]) # (word, step)

        if not word_set:
            return 0
        
        while word_candidates:
            current_word, current_step = word_candidates.popleft()

            if current_word == endWord:
                return current_step
            
            for i in range(len(current_word)):
                for char in ascii_lowercase:
                    if char == current_word[i]:
                        continue

                    next_word_processed = list(current_word)
                    next_word_processed[i] = char
                    next_word = "".join(next_word_processed)
                    next_step = current_step + 1

                    if next_word in word_set and next_word not in word_used:
                        word_candidates.append((next_word, next_step))
                        word_used.add(next_word)
        
        return 0
```
