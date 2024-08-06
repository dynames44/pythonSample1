from copy import copy

# 집합 (set) 생성 및 선언
setData1 = {'ABC', 'BCD', 'DEF'}
setData2 = set(['DEF', 'FGH', 'HIG'])

# 객체 복사 (두 가지 방법)
setData3 = copy(setData2)  # copy 모듈을 사용한 복사
setData4 = setData2.copy()  # set의 copy 메서드를 사용한 복사

# 항목 추가 (setData2에 새로운 항목 추가)
setData2.add("ZZZ")
setData2.add("WWW")

# 집합을 리스트로 변환 및 정렬
listData1 = list(setData1)
listData1.sort()  # 리스트를 오름차순으로 정렬

# 집합을 튜플로 변환 및 다시 리스트로 변환
tupleData1 = tuple(setData2)  # setData2를 튜플로 변환
listData2 = list(tupleData1)  # 튜플을 다시 리스트로 변환

# 항목 삭제: 존재하지 않는 항목을 삭제해도 에러가 발생하지 않음
setData2.discard(2)  # 2는 setData2에 없으므로 아무 일도 일어나지 않음
setData2.discard('ZZZ')  # 'ZZZ'는 존재하므로 삭제됨

# 항목 삭제: 존재하지 않는 항목을 삭제하려 하면 에러가 발생
setData2.remove("WWW")  # 'WWW'는 존재하므로 삭제됨
# setData2.remove("WWW1")    # 'WWW1'은 존재하지 않으므로 에러 발생

print("집합 --------------------------------------------")
print("setData1::::", setData1)
print("setData2::::", setData2)
# print("setData3::::", setData3)
# print("setData4::::", setData4)
# print("listData1::::", listData1)
# print("tupleData1::::", tupleData1)
# print("listData2::::", listData2)
print("")

# 교집합
print("교집합 --------------------------------------------")
print("intersection Type1::::", setData1 & setData2)  # 방법 1: & 연산자를 사용한 교집합 구하기
print("intersection Type2::::", setData1.intersection(setData2))  # 방법 2: intersection() 메서드를 사용한 교집합 구하기
print("")

# 합집합
print("합집합 --------------------------------------------")
print("union Type1::::", setData1 | setData2) # Type1: '|' 연산자를 사용한 방법
print("union Type2::::", setData1.union(setData2)) # Type2: union() 메서드를 사용한 방법
print("")

# 차집합
print("차집합 --------------------------------------------")
print("difference Type1::::", setData1 - setData2) # Type1: '-' 연산자를 사용한 방법
print("difference Type2::::", setData1.difference(setData2)) # Type2: difference() 메서드를 사용한 방법
print("")

# 집합값을 변경
print("집합값 수정 --------------------------------------------")
setData1.update({"AAA"})  # 집합에 요소를 추가
print("update setData1::::", setData1)

setData1.intersection_update(setData2)  # 두 집합의 교집집합 결과로 변경
print("intersection_update setData1::::", setData1)