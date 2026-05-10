# 02｜条件分岐（if / elif / else）【初級】

## 📋 問題

コマンドライン引数で点数（0〜100）を受け取り、成績を判定して出力する `answer.py` を作成してください。

| 点数 | 出力 |
|------|------|
| 90以上 | `S: 優秀です！` |
| 70以上90未満 | `A: 合格です` |
| 50以上70未満 | `B: もう少し` |
| 50未満 | `C: 要復習` |

**実行例:**
```bash
python3 answer.py 95   # → S: 優秀です！
python3 answer.py 72   # → A: 合格です
python3 answer.py 55   # → B: もう少し
python3 answer.py 30   # → C: 要復習
```

---

## 💡 ヒント

```python
import sys
score = int(sys.argv[1])   # 引数を整数に変換

if score >= 90:
    print("S: 優秀です！")
elif score >= 70:
    ...
```

`sys.argv[1]` でシェルから渡した引数を受け取れます。
`int()` で文字列を整数に変換するのを忘れずに！

---

## ✅ 回答例

```python
# answer.py
import sys

score = int(sys.argv[1])

if score >= 90:
    print("S: 優秀です！")
elif score >= 70:
    print("A: 合格です")
elif score >= 50:
    print("B: もう少し")
else:
    print("C: 要復習")
```

---

## 📚 解説

| 要素 | 説明 |
|------|------|
| `if 条件:` | 条件が True のときに実行 |
| `elif 条件:` | 前の条件が False で、この条件が True のとき |
| `else:` | どの条件にも当てはまらないとき |
| `>=` `<=` `>` `<` `==` `!=` | 比較演算子 |

**ポイント:** `elif` は上から順に評価されます。`score >= 70` は「70以上」ですが、その前に `>= 90` が False だった場合のみ評価されるので、自動的に「70以上90未満」になります。

---

## 🚀 実行方法

```bash
cd 02-if-elif-else
python3 answer.py 95

# まとめてテストしたいとき
for score in 100 89 70 69 50 49 0; do
  echo -n "score=$score → "; python3 answer.py $score
done
```
