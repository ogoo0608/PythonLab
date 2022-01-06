# 202135317 김정준

import random

count = 0
diceA, diceB, diceC = 0, 0, 0

while True:
    count += 1
    diceA = random.randint(1,6)
    diceB = random.randint(1,6)
    diceC = random.randint(1,6)

    if (diceA == diceB) and (diceB == diceC):
        break

print("3개 주사위는 모두", diceA, "입니다.")
print("같은 숫자가 나오기까지", count, "번 던졌습니다.")
