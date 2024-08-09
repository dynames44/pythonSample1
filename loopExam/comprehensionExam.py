
#Comprehension (컴프리헨션)
#list, dictionary, set에서 사용
#반복문과 조건문을 결합하여 하나의 구문으로 사용.

# Synx : [expression for item in iterable if condition]
# - expression: 각 아이템에 적용할 표현식입니다.(사용변수)
# - item: 반복 가능한 객체(iterable)에서 각 항목을 나타냅니다.
# - iterable: 리스트, 튜플, 문자열 등 반복 가능한 객체입니다.
# - condition: (선택 사항) 특정 조건을 만족하는 항목만 포함시키기 위한 조건문입니다.

# Comprehension 사용 리스트 값 생성
print("Comprehension list ::::::")
listData1 = [i for i in range(1, 11)] # 1부터 10까지 생성
print("listData1 ::::::",listData1)
print()

#조건절 적용
print("list condition::::::")
listData1 = [i for i in listData1 if i % 2 ==0] #짝수만 변수에 담는다
print("list condition ::::::",listData1)

# 중첩 조건절 적용
listData1 = [i for i in range(1, 11) if i % 2 == 0 if i < 5] #5보다 작은 수 중 짝수만 변수에 담는다
print("list dual condition ::::::",listData1)

# else 조건문
listData2 = [i * 2 if i % 2 == 0 else i for i in range(1, 11)] # 짝수는 *2 그외는 값 그대로
print("list else condition ::::::",listData2)
print()

#2차원 리스트 단일 리스트
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("type1 ::::::",flattened)

# 중첩변수
data = [(x, y) for x in range(1, 6) for y in range(1, 4)]
print("type2 ::::::",data)

# 중첩변수 조건절
data = [(x, y) for x in range(1, 4) for y in range(1, 4) if x % 2 == 1 if y > 1]
print("type3 ::::::",data)
print()

# Comprehension 사용 딕셔너리 값 생성
print("Comprehension dictionary ::::::")
name = ["왕춘삼", "김덕팔", "황갑득"]
age = [23, 14, 42]
dictData1 = {key: value for key in name for value in age}
dictData2 = {key: value for (key, value) in zip(name, age)} #리스트를 zip으로 묵어 간결하게 사용

print("dictData1 ::::::",dictData1)
print("dictData2 ::::::",dictData2)
print()

print("dictionary condition::::::")
dictData3 = {key: value for (key, value) in zip(name, age)  if value > 20}
print("dictData3 ::::::",dictData3)
