import json

#読み込み
def load_todos():
    try:
        with open("todos.json","r",encoding="utf-8") as f:
            todos = json.load(f)
    except FileNotFoundError:
        todos = []
    return todos

#書き込み
def save_todos(todos):
    with open("todos.json","w",encoding="utf-8") as f:
        json.dump(todos,f,ensure_ascii=False,indent=2)

#メニュー画面
def show_menu(todos):
    total = len(todos)
    done_total = 0
    for todo in todos:
        if todo["done"]:
            done_total += 1
    print("=============================")
    print("   📝 TODO リストアプリ")
    print("=============================")
    print(f"タスク数:{total}(完了:{done_total}件)\n")
    print("1.タスクを追加する")
    print("2.タスクの一覧を見る")
    print("3.タスクを完了にする")
    print("4.タスクを削除する")
    print("5.終了する\n")

#タスクを追加する
def add_todo(todos):
    title = input("タスク名を入力:")
    task = {
        "id": len(todos) + 1,
        "title": title,
        "done": False
    }
    todos.append(task)
    save_todos(todos)
    print(f"✅ 「{title}」を追加しました!")

#タスクの一覧を見る
def show_todos(todos):
    if not todos:
        print("タスクはありません")
    else:
        print("=== TODOリスト ===\n")
        for i,todo in enumerate(todos,1):
            if todo["done"]:
                checkbox = "✅"
                status = "(完了)"
            else:
                checkbox = "⬜️"
                status = ""
            print(f"[{i}]{checkbox}{todo['title']}{status}")
    input("Enterを押すとメニューに戻ります")

#タスクを完了にする
def complete_todo(todos):
    show_todos(todos)
    if not todos:
        return
    try:
        num = int(input("完了にするタスク番号を入力:"))
        if 1<= num <= len(todos):
            todo = todos[num - 1]
            if todo["done"]:
                print(f"{todo['title']}は完了しています")
            else:
                todo["done"] = True
                save_todos(todos)
                print(f"✅ 「{todo['title']}」を完了にしました!")
        else:
            print("無効なタスク番号です")
    except ValueError:
        print("数字を入力してください")

#タスクを削除する
def delete_todo(todos):
    show_todos(todos)
    if not todos:
        return
    try:
        num = int(input("削除するタスク番号を入力:"))
        if 1<= num <= len(todos):
            removed = todos.pop(num - 1)
            save_todos(todos)
            print(f"🗑「{removed['title']}」を削除しました。")
        else:
            print("無効なタスク番号です")
    except ValueError:
        print("数字を入力してください")

def main ():
    todos = load_todos()
    while True:
        show_menu(todos)
        try:
            choice = int(input("選択してください(1-5):"))
            if 1 <= choice <= 5:
                if choice == 1:
                    add_todo(todos)
                elif choice == 2:
                    show_todos(todos)
                elif choice == 3:
                    complete_todo(todos)
                elif choice == 4:
                    delete_todo(todos)
                elif choice == 5:
                    break
            else:
                print("無効なタスク番号です")
        except ValueError:
            print("数字を入力してください")

if __name__ == "__main__":
    main()