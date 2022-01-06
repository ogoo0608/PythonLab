# 202135317 김정준

import random

myhand = input("나의 가위/바위/보 ==>")

pchand = random.choice(["가위", "바위", "보"])
print("컴퓨터의 가위/바위/보", pchand)

if myhand == "가위" :
    if pchand == "가위" :
        print("비겼습니다.")
    elif pchand == "바위":
        print("졌습니다. ㅠㅠ")
    elif pchand == "보":
        print("이겼습니다. ^^")
elif myhand == "바위" :
    if pchand == "보":
        print("졌습니다. ㅠㅠ")
    elif pchand == "가위":
        print("이겼습니다. ^^")
    elif pchand == "바위":
        print("비겼습니다.")
elif myhand == "보" :
    if pchand == "가위":
        print("졌습니다. ㅠㅠ")
    elif pchand == "바위":
        print("이겼습니다. ^^")
    elif pchand == "보":
        print("비겼습니다.")

else :
    print("가위/바위/보 중 하나를 내세요 .. ^^")
