# 202135317 김정준

print(" ## 택배를 보내기위한 정보를 입력하세요 ##")
personName = input("받는 사람 : ")
personAddress = input("주소 : ")
weight = int(input("무게(g) : "))

print(" ** 받는 사람 ==> ", personName)
print(" ** 주소 ==> ", personAddress)
print(" ** 배송비 ==>", weight*5, "원")
