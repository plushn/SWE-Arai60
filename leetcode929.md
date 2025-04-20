# 929. Unique Email Addresses

## Step1

- 何度か文法ミスがあったが、強引ではあるが自力でacceptまでたどり着けた。
- [文字列演算子+](https://docs.python.org/ja/3/library/stdtypes.html#common-sequence-operations)と[join](https://docs.python.org/ja/3/library/stdtypes.html#str.join)を確認。
- ちなみに、`1 <= emails[i].length <= 100`の制限があるが、Gmailの場合、[ユーザー名が6文字から30文字まで](https://support.google.com/mail/community-guide/257098940/gmail%E3%81%AE%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E3%81%AE%E4%BB%95%E7%B5%84%E3%81%BF-%E3%83%94%E3%83%AA%E3%82%AA%E3%83%89%E3%81%AE%E6%9C%89%E7%84%A1%E3%82%84%E3%82%A8%E3%82%A4%E3%83%AA%E3%82%A2%E3%82%B9%E3%81%A7%E3%81%A9%E3%81%86%E3%81%AA%E3%82%8B%E3%81%8B?hl=ja#:~:text=Gmail%E3%81%AE%E5%A0%B4%E5%90%88%E3%81%AF%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC,%E7%9A%84%E3%81%AB%E6%B1%BA%E3%81%BE%E3%81%A3%E3%81%A6%E3%81%84%E3%81%BE%E3%81%99%E3%80%82)とのこで、100文字以内のメールアドレスは妥当な想定か。

```python
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_addresses = set()
        for email in emails:
            index = 0
            address = ""
            while email[index] != "@":
                if email[index] == ".":
                    index += 1
                    continue
                if email[index] == "+":
                    while email[index] != "@":
                        index += 1
                    break
                address += email[index]             
                index += 1
            address += email[index:]
            unique_addresses.add(address)
        return len(unique_addresses)
```

## Step2

### splitやreplaceで分解

- localとdomainを分離[splitやreplace](https://docs.python.org/ja/3/library/stdtypes.html#str.split)で分解する。
- これは入力されるサイトで弾かれる処理になるかもしれないが、@がない場合を考慮した。

```python
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_addresses = set()
        for email in emails:
            if "@" not in email:
                raise ValueError(f" {email}is not a valid email address")
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique_addresses.add("".join([local, "@", domain]))
        return len(unique_addresses)
```

### 正規表現

- [正規表現](https://docs.python.org/ja/3/library/re.html#re.sub)を知らなかったためドキュメントを確認した。
- 正規表現にもsplitはあるようだが、今回は他の実装例を参考にsubを使用した。
- [f-string](https://docs.python.org/ja/3/reference/lexical_analysis.html#formatted-string-literals)

```python
import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_addresses = set()
        for address in emails:
            local, domain = address.split('@', maxsplit = 1)
            local = re.sub(r'\+.*', '', local)
            local = re.sub(r'\.', '', local)
            unique_addresses.add(f"{local}@{domain}")
        return len(unique_addresses)
```

## Step3

- 正規表現などを勉強すると、step1の解答は力技であったなと痛感した。また、splitを使いこなせておらずlocalとdomainを分離する処理ができていなかった。正規表現を使用して3回解き直す。
- 1回目 5分
- 2回目 4分
- 3回目 4分
