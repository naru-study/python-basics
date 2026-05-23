students = [
    {"name": "田中", "score": 88},
    {"name": "鈴木", "score": 72},
    {"name": "佐藤", "score": 95},
    {"name": "山田", "score": 60},
    {"name": "伊藤", "score": 78},
]
#1. **全員の点数を表示**する
title = "=== 全員の点数 ==="
print(title)

for student in students:
    print(f"{student['name']}:{student['score']}点")

#2. **平均点**を計算して表示する
total = 0 
for student in students:
    total += student["score"]

average = total / len(students)
print(f"平均点:{average}点")


total = sum(student["score"] for student in students)
average = total / len(students)
print(f"平均点:{average}点")

#3. **平均点以上**の生徒だけ表示する
title = "=== 平均点以上 ==="
print(title)

for student in students:
    if student["score"] >= average:
        print(f"{student['name']}:{student['score']}点")

#4. **点数の高い順**に並べて表示する
title = "=== 点数順 (高い順)==="
print(title)

sorted_score = sorted(students,key=lambda student: student["score"],reverse=True)
for student in sorted_score:
    print(f"{student['name']}:{student['score']}点")