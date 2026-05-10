# 06｜ファイル読み書き・例外処理【中級】

## 📋 問題

`scores.txt` というファイルを読み込み、集計結果を `result.txt` に書き出す `answer.py` を作成してください。

### scores.txt（自分で作成してください）
```
田中,88
鈴木,72
佐藤,abc
山田,60
伊藤,78
```

※ `佐藤,abc` のように数値でない行はスキップ（警告を表示）する

### result.txt（期待する出力）
```
=== 集計結果 ===
田中: 88点
鈴木: 72点
山田: 60点
伊藤: 78点

合計: 298点
平均: 74.5点
最高点: 佐藤 88点
```

### 例外処理の要件
- `scores.txt` が存在しない → `エラー: ファイルが見つかりません` と表示して終了
- 数値に変換できない行 → `警告: "佐藤,abc" をスキップしました` と表示してスキップ

---

## 💡 ヒント

```python
# ファイルを安全に開く
try:
    with open("scores.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("エラー: ファイルが見つかりません")
    exit()

# 書き込み
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("=== 集計結果 ===\n")

# カンマ区切りの分割
name, score_str = line.strip().split(",")
```

---

## ✅ 回答例

```python
# answer.py

# まず scores.txt を作成して実行してください
# printf "田中,88\n鈴木,72\n佐藤,abc\n山田,60\n伊藤,78\n" > scores.txt

def load_scores(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("エラー: ファイルが見つかりません")
        exit()

    students = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            name, score_str = line.split(",")
            students.append({"name": name, "score": int(score_str)})
        except ValueError:
            print(f"警告: \"{line}\" をスキップしました")
    return students

def write_result(students, filename):
    total = sum(s["score"] for s in students)
    avg   = total / len(students)
    top   = max(students, key=lambda s: s["score"])

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== 集計結果 ===\n")
        for s in students:
            f.write(f"{s['name']}: {s['score']}点\n")
        f.write(f"\n合計: {total}点\n")
        f.write(f"平均: {avg}点\n")
        f.write(f"最高点: {top['name']} {top['score']}点\n")

    print(f"結果を {filename} に書き出しました。")

students = load_scores("scores.txt")
write_result(students, "result.txt")
```

---

## 📚 解説

| 要素 | 説明 |
|------|------|
| `with open(...) as f:` | ファイルを安全に開く（自動でclose） |
| `f.readlines()` | 全行をリストで取得 |
| `line.strip()` | 行末の改行・空白を除去 |
| `try / except FileNotFoundError` | ファイルなしエラーを捕捉 |
| `try / except ValueError` | 型変換エラーを捕捉 |
| `max(list, key=...)` | 最大値の要素を取得 |

---

## 🚀 実行方法

```bash
cd 06-file-exception

# テスト用の scores.txt を作成
printf "田中,88\n鈴木,72\n佐藤,abc\n山田,60\n伊藤,78\n" > scores.txt

# 実行
python3 answer.py

# 結果を確認
cat result.txt

# エラーケースのテスト（ファイルなし）
rm scores.txt && python3 answer.py
```
