# 변수에 값 저장하고 출력하기
name = "Alice"
age = 25
print("이름:", name)
print("나이:", age)

# 숫자가 짝수인지 홀수인지 판별하기
num = 7
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 1부터 5까지 출력하기
for i in range(1, 6):
    print(i)

# 두 수를 더하는 함수 만들기
def add(a, b):
    return a + b

result = add(3, 5)
print("결과:", result)

# 리스트의 모든 요소 출력하기
fruits = ["사과", "바나나", "포도"]
for fruit in fruits:
    print(fruit)