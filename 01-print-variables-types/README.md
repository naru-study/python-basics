# 01｜print・変数・型【超入門】

## 📋 問題

以下の変数を使って、指定の形式で出力する `answer.py` を作成してください。

**使う変数:**
- `name` = 自分の名前（文字列）
- `age` = 自分の年齢（整数）
- `height` = 自分の身長（小数）
- `is_student` = 学生かどうか（True / False）

**期待する出力:**
```
名前: 田中 太郎
年齢: 25 歳
身長: 170.5 cm
学生: True
名前の型: <class 'str'>
年齢の型: <class 'int'>
```

---

## 💡 ヒント

```python
name      = "田中 太郎"   # str  型：文字列は "" で囲む
age       = 25            # int  型：整数
height    = 170.5         # float型：小数
is_student = True         # bool 型：True / False

print(f"名前: {name}")          # f文字列で変数を埋め込む
print(type(name))               # 型を調べる → <class 'str'>
```

---

## ✅ 回答例

```python
# answer.py
name       = "田中 太郎"
age        = 25
height     = 170.5
is_student = True

print(f"名前: {name}")
print(f"年齢: {age} 歳")
print(f"身長: {height} cm")
print(f"学生: {is_student}")
print(f"名前の型: {type(name)}")
print(f"年齢の型: {type(age)}")
```

---

## 📚 解説

| 型 | 例 | 説明 |
|----|----|------|
| `str` | `"田中"` | 文字列。`""` で囲む |
| `int` | `25` | 整数 |
| `float` | `170.5` | 小数点あり |
| `bool` | `True` / `False` | 真偽値。大文字始まり |

`type()` 関数を使うと変数の型を確認できます。  
`f"...{変数}..."` の形式（f文字列）で変数を文字列に埋め込めます。

---

## 🚀 実行方法

```bash
cd 01-print-variables-types
python3 answer.py
```
