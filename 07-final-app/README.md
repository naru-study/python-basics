# 07｜🏆 総合課題：TODOリストアプリ

## 🎯 課題の目標

これまで学んだ **全ての文法** を使って、シェル上で動く TODOリスト管理アプリ を作成してください。

使う文法:
- ✅ print・変数・型（01）
- ✅ if / elif / else（02）
- ✅ for / while ループ（03）
- ✅ 関数（def）（04）
- ✅ リスト・辞書（05）
- ✅ ファイル読み書き・例外処理（06）

---

## 📋 アプリの仕様

### 起動方法
```bash
python3 todo.py
```

### メニュー画面
```
=============================
    📝 TODO リストアプリ
=============================
タスク数: 3件（完了: 1件）

1. タスクを追加する
2. タスクの一覧を見る
3. タスクを完了にする
4. タスクを削除する
5. 終了する

選択してください (1-5): 
```

### 各機能の動作

**1. タスクを追加する**
```
タスク名を入力: 牛乳を買う
✅ 「牛乳を買う」を追加しました！
```

**2. タスクの一覧を見る**
```
=== TODO リスト ===
[1] ✅ 牛乳を買う（完了）
[2] ⬜ 洗濯をする
[3] ⬜ メールを返す
```

**3. タスクを完了にする**
```
完了にするタスク番号を入力: 2
✅ 「洗濯をする」を完了にしました！
```

**4. タスクを削除する**
```
削除するタスク番号を入力: 3
🗑 「メールを返す」を削除しました。
```

### データの保存
- タスクは `todos.json` に自動保存される
- アプリを再起動してもタスクが残る

---

## 💡 設計のヒント

### データ構造
```python
# 1つのタスクは辞書で表す
task = {
    "id": 1,
    "title": "牛乳を買う",
    "done": False
}

# タスクのリスト
todos = [task1, task2, ...]
```

### ファイル保存（JSON）
```python
import json

# 保存
with open("todos.json", "w", encoding="utf-8") as f:
    json.dump(todos, f, ensure_ascii=False, indent=2)

# 読み込み
try:
    with open("todos.json", "r", encoding="utf-8") as f:
        todos = json.load(f)
except FileNotFoundError:
    todos = []   # ファイルがなければ空リストから始める
```

### 関数の分け方（例）
```python
def load_todos():       # ファイルから読み込む
def save_todos(todos):  # ファイルに書き出す
def show_todos(todos):  # 一覧を表示する
def add_todo(todos):    # タスクを追加する
def complete_todo(todos): # タスクを完了にする
def delete_todo(todos): # タスクを削除する
def show_menu(todos):   # メニューを表示する
def main():             # アプリのメインループ
```

---

## ✅ 回答例

```python
# todo.py
import json

FILENAME = "todos.json"

def load_todos():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def show_todos(todos):
    if not todos:
        print("タスクはまだありません。")
        return
    print("\n=== TODO リスト ===")
    for i, task in enumerate(todos, start=1):
        mark = "✅" if task["done"] else "⬜"
        status = "（完了）" if task["done"] else ""
        print(f"[{i}] {mark} {task['title']}{status}")
    print()

def add_todo(todos):
    title = input("タスク名を入力: ").strip()
    if not title:
        print("タスク名が空です。")
        return
    todos.append({"title": title, "done": False})
    save_todos(todos)
    print(f"✅ 「{title}」を追加しました！")

def complete_todo(todos):
    show_todos(todos)
    try:
        num = int(input("完了にするタスク番号を入力: "))
        task = todos[num - 1]
        task["done"] = True
        save_todos(todos)
        print(f"✅ 「{task['title']}」を完了にしました！")
    except (ValueError, IndexError):
        print("無効な番号です。")

def delete_todo(todos):
    show_todos(todos)
    try:
        num = int(input("削除するタスク番号を入力: "))
        task = todos.pop(num - 1)
        save_todos(todos)
        print(f"🗑 「{task['title']}」を削除しました。")
    except (ValueError, IndexError):
        print("無効な番号です。")

def show_menu(todos):
    total = len(todos)
    done  = sum(1 for t in todos if t["done"])
    print("\n=============================")
    print("    📝 TODO リストアプリ")
    print("=============================")
    print(f"タスク数: {total}件（完了: {done}件）\n")
    print("1. タスクを追加する")
    print("2. タスクの一覧を見る")
    print("3. タスクを完了にする")
    print("4. タスクを削除する")
    print("5. 終了する")

def main():
    todos = load_todos()
    while True:
        show_menu(todos)
        choice = input("\n選択してください (1-5): ").strip()
        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            show_todos(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            print("👋 終了します。")
            break
        else:
            print("1〜5 の数字を入力してください。")

if __name__ == "__main__":
    main()
```

---

## 📚 使った文法の整理

| 文法 | どこで使った？ |
|------|---------------|
| print・f文字列 | メニュー表示・各メッセージ |
| 変数・型 | `FILENAME`・`total`・`done` など |
| if / elif / else | メニュー選択・入力バリデーション |
| for ループ | タスク一覧の表示 |
| while ループ | メインループ（アプリが動き続ける） |
| 関数（def） | 機能ごとに関数を分割 |
| リスト・辞書 | タスクデータの管理 |
| ファイル・例外処理 | JSON の読み書き・エラー対応 |

---

## 🚀 実行方法

```bash
cd 07-final-app
python3 todo.py
```

## 🔥 余裕があれば挑戦しよう（発展課題）

- [ ] タスクに **期限**（due date）を追加できるようにする
- [ ] 期限が過ぎたタスクに ⚠️ を表示する
- [ ] タスクを **カテゴリ**（仕事・プライベートなど）で分類できるようにする
- [ ] 完了済みのタスクをまとめて削除できるようにする
