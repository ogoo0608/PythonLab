# 202135317 김정준

i = 0
fact = 1
students_num = 5

for i in range(1, students_num + 1, 1):
    fact = fact * i

print("A, B, C, D, E 학생들을 순서대로 세우는 경우의 수 : " , fact)
