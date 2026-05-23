try:
    with open("scores.txt","r",encoding="utf-8") as f:
        lines = f.readlines()
        cleaned = [line.strip() for line in lines]
except FileNotFoundError:
    print("エラー: ファイルが見つかりません")
    exit()

students = []

for clean in cleaned:
    name, score_str = clean.split(",")

    try:
        score = int(score_str)
    except ValueError:
        print(f"警告:\"{clean}\"をスキップしました")
        continue
    students.append({
        "name": name,
        "score": score
    })

# for student in students:
#     print(f"{student['name']}:{student['score']}点")

total = 0
for student in students:
    total += student["score"]
# print(f"合計:{total}点")

average = total / len(students)
# print(f"平均:{average}点")

top_student = max(students,key=lambda student: student["score"])
# print(f"最高点:{top_student['name']} {top_student['score']}点")

with open("result.txt","w",encoding="utf-8") as f:
        f.write("=== 集計結果 ===\n")

        for student in students:
            f.write(f"{student['name']}:{student['score']}点\n")

        f.write("\n") 
        f.write(f"合計:{total}点\n")
        f.write(f"平均:{average}点\n")
        f.write(f"最高点:{top_student['name']} {top_student['score']}点\n")