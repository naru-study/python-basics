# 04｜関数（def）【初中級】

## 📋 問題

以下の3つの関数を実装した `answer.py` を作成してください。

### `greet(name, lang="ja")`
- `lang="ja"` のとき → `こんにちは、○○ さん！`
- `lang="en"` のとき → `Hello, ○○!`

### `is_prime(n)`
- `n` が素数なら `True`、そうでなければ `False` を返す

### `fizzbuzz(n)`
- 1〜n の FizzBuzz 結果をリストで返す

**期待する出力:**
```
こんにちは、太郎 さん！
Hello, Taro!
True
False
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
```

---

## 💡 ヒント

```python
def greet(name, lang="ja"):      # lang は省略可能（デフォルト値あり）
    if lang == "ja":
        return f"こんにちは、{name} さん！"
    ...

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):        # 2〜n-1 で割り切れるか調べる
        if n % i == 0:
            return False
    return True
```

---

## ✅ 回答例

```python
# answer.py

def greet(name, lang="ja"):
    if lang == "ja":
        return f"こんにちは、{name} さん！"
    elif lang == "en":
        return f"Hello, {name}!"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# 動作確認
print(greet("太郎"))
print(greet("Taro", lang="en"))
print(is_prime(7))
print(is_prime(8))
print(fizzbuzz(10))
```

---

## 📚 解説

| 要素 | 説明 |
|------|------|
| `def 関数名(引数):` | 関数を定義する |
| `return 値` | 関数の戻り値を指定する |
| `def func(x, y="default")` | デフォルト引数（省略可能な引数） |
| `list.append(値)` | リストの末尾に要素を追加する |

---

## 🚀 実行方法

```bash
cd 04-functions
python3 answer.py

# 特定の関数だけテスト
python3 -c "from answer import is_prime; print(is_prime(97))"
python3 -c "from answer import fizzbuzz; print(fizzbuzz(15))"
```
