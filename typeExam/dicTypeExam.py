# 딕셔너리 생성 및 선언
listData = []
dictData3 = {} # 빈 딕셔너리 생성, dict()를 사용 하는거 보다 자원사용, 속도에서 효율적
dictData1 = {'seqId':'001', 'name' : 'name001', 'phoneNo' : '010-1010-0001'}
dictData2 = dict(seqId="002", name="name002", phoneNo = "010-2020-0002")

print("생성 --------------------------------------------")
print("dictData1:::", dictData1)
print("dictData2:::", dictData2)
print("dictData3:::", dictData3)
print("")

# 딕셔너리 항목추가
dictData3["seqId"] = "0003" #딕셔너리 [키] = 값
dictData3["name"] = "name003"
dictData3["phoneNo"] = "010-3030-0003"

# 딕셔너리 데이터 접근 방법
print("딕셔너리 데이터 접근 방법 --------------------------------------------")
print("Get Method:::", dictData3.get("seqId")) #get 메서드를 사용하여 접근
print("Get Key Value:::", dictData3["name"]) #키값 사용하여 접근
print("Data Get Default::", dictData3.get("test","nope")) #딕셔너리에 해당 키가 없을때 기본값 설정
print("")

# 딕셔너리 키 존재 여부 확인
print("딕셔너리 키 존재 여부 확인 --------------------------------------------")
print("Key Exist:::", "seqId" in dictData3) #딕셔너리에 있는 Key : True
print("Key Not Exist:::", "test" in dictData3) #딕셔너리에 없는 Key : False
print("")

# 딕셔너리 메서드 활용
print("딕셔너리 메서드 #1 --------------------------------------------")
dictData4 = dictData3.copy() # 딕셔너리 복사
print("dictData4 #1:::", dictData4)
dictData4["seqId"] = "0004" #키값 수정
del dictData4["phoneNo"]  #키 삭제
print("dictData4 #2:::", dictData4)
dictData4.clear() # 딕셔너리의 모든 항목 삭제
print("dictData4 #3:::", dictData4)

# 딕셔너리가 비어 있는지 확인
if dictData4:
    print("dict Not Empty")
else:
    print("dict Empty")
print("")

print("딕셔너리 메서드 #2 --------------------------------------------")
dictData5 = dictData3.copy() # 딕셔너리 복사
print("딕셔너리 Key 반환:::", dictData5.keys())
print("딕셔너리 Value 반환:::", dictData5.values())
print("딕셔너리 Key/Value 반환:::", dictData5.items())
print("딕셔너리 항목 list 변환:::", list(dictData5.keys()))
print("딕셔너리 Key/Value list 변환:::", type(list(dictData5.items())[0])) #items은 튜플 type로 반환 된다.