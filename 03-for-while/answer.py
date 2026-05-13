### 問題A: FizzBuzz（for ループ）
for i in range(1,31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

### 問題B: 合計（while ループ）
count, total = 0, 0
while total <= 100:
    count = count + 1
    total = total + count
    print(f"{count}回目: total = {total}")
print(f"{count}回目で100を超えました!")
