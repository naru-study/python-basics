import sys
score = int(sys.argv[1])

if score >= 90:
    print("S: 優秀です!")
elif score >= 70:
    print("A: 合格です")
elif score >= 50:
    print("B: もう少し")
else:
    print("C: 要復習")
