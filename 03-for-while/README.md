# 03｜ループ（for / while）【初級】

## 📋 問題

以下の2つを `answer.py` に実装してください。

### 問題A: FizzBuzz（for ループ）

1〜30 を順に出力する。ただし：
- 3の倍数 → `Fizz`
- 5の倍数 → `Buzz`
- 両方の倍数 → `FizzBuzz`

**期待する出力（先頭15行）:**
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

### 問題B: 合計（while ループ）

`total = 0` から始めて、`total` が 100 を超えるまで整数を足し続け、
何回で超えたか・最終的な合計を出力する。

```
1回目: total = 1
2回目: total = 3
3回目: total = 6
...
14回目: total = 105
14回で100を超えました！
```

---

## 💡 ヒント

```python
# for ループ
for i in range(1, 31):     # 1〜30
    if i % 15 == 0:        # % は余り。15の倍数を先に！
        print("FizzBuzz")

# while ループ
count = 0
total = 0
while total <= 100:
    count += 1
    total += count
```

---

## ✅ 回答例

```python
# answer.py

# --- 問題A: FizzBuzz ---
print("=== FizzBuzz ===")
for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# --- 問題B: while で合計 ---
print("\n=== while ループ ===")
count = 0
total = 0
while total <= 100:
    count += 1
    total += count
    print(f"{count}回目: total = {total}")

print(f"{count}回で100を超えました！")
```

---

## 📚 解説

| 要素 | 説明 |
|------|------|
| `range(1, 31)` | 1〜30 の連番（31は含まない） |
| `%` | 余り演算子。`i % 3 == 0` → 3の倍数 |
| `while 条件:` | 条件が True の間ループし続ける |
| `count += 1` | `count = count + 1` の省略形 |

---

## 🚀 実行方法

```bash
cd 03-for-while
python3 answer.py

# FizzBuzz の出力を確認
python3 answer.py | grep -n "FizzBuzz"   # 15行目・30行目に出るはず
python3 answer.py | head -15 | wc -l    # 最初の15行あるか確認
```
