# 202135317 김정준

import random

wiseSay = [
"삶이 있는 한 희망은 있다",
"언제나 현재에 집중할 수 있다면 행복할 것이다",
"신은 용기있는 자를 결코 버리지 않는다",
"피할 수 없으면 즐겨라",
"행복한 삶을 살기 위해 필요한 것은 거의 없다",
"내일은 내일의 태양이 뜬다",
"행복은 습관이다. 그것을 몸에 지녀라",
"1퍼센트의 가능성, 그것이 나의 길이다",
"작은 기회로부터 종종 위대한 업적이 시작된다" ]

today = random.randint(0, len(wiseSay)-1)

print("오늘의 명언 ==>", wiseSay[today])