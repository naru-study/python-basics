# 05｜リスト・辞書【初中級】

## 📋 問題

以下の成績データを使って `answer.py` を作成してください。

```python
students = [
    {"name": "田中", "score": 88},
    {"name": "鈴木", "score": 72},
    {"name": "佐藤", "score": 95},
    {"name": "山田", "score": 60},
    {"name": "伊藤", "score": 78},
]
```

### やること

1. **全員の点数を表示**する
2. **平均点**を計算して表示する
3. **平均点以上**の生徒だけ表示する
4. **点数の高い順**に並べて表示する

**期待する出力:**
```
=== 全員の点数 ===
田中: 88点
鈴木: 72点
佐藤: 95点
山田: 60点
伊藤: 78点

平均点: 78.6点

=== 平均点以上 ===
田中: 88点
佐藤: 95点
伊藤: 78点

=== 点数順（高い順）===
佐藤: 95点
田中: 88点
伊藤: 78点
鈴木: 72点
山田: 60点
```

---

## 💡 ヒント

```python
# リストのループ
for s in students:
    print(s["name"], s["score"])   # 辞書のキーでアクセス

# 平均
scores = [s["score"] for s in students]   # リスト内包表記
avg = sum(scores) / len(scores)

# フィルタ（平均以上）
above = [s for s in students if s["score"] >= avg]

# 並び替え
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
```

---

## ✅ 回答例

```python
# answer.py
students = [
    {"name": "田中", "score": 88},
    {"name": "鈴木", "score": 72},
    {"name": "佐藤", "score": 95},
    {"name": "山田", "score": 60},
    {"name": "伊藤", "score": 78},
]

print("=== 全員の点数 ===")
for s in students:
    print(f"{s['name']}: {s['score']}点")

scores = [s["score"] for s in students]
avg = sum(scores) / len(scores)
print(f"\n平均点: {avg}点")

print("\n=== 平均点以上 ===")
for s in students:
    if s["score"] >= avg:
        print(f"{s['name']}: {s['score']}点")

print("\n=== 点数順（高い順）===")
for s in sorted(students, key=lambda s: s["score"], reverse=True):
    print(f"{s['name']}: {s['score']}点")
```

---

## 📚 解説

| 要素 | 説明 |
|------|------|
| `{"key": value}` | 辞書。キーで値にアクセスする |
| `[x for x in list]` | リスト内包表記 |
| `[x for x in list if 条件]` | 条件付きリスト内包表記（フィルタ） |
| `sorted(list, key=..., reverse=True)` | リストを並び替える |
| `lambda s: s["score"]` | 無名関数。並び替えの基準に使う |

---

## 🚀 実行方法

```bash
cd 05-list-dict
python3 answer.py
```
