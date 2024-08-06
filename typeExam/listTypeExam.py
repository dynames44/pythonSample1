
#리스트 생성 & 할당
dataList1 = [] #빈 리스트 생성
dataList2 = [1,3,7,2] #리스트 생성 & 값 할당
dataList3 = [1,2,3, ['test','comp']] #리스트는 다른 리스트를 인자로 가질수 있다
dictList = []
dictData1 = {'seqId':'001', 'name' : 'name001', 'phoneNo' : '010-1010-0001'}
dictData2 = dict(seqId="002", name="name002", phoneNo = "010-2020-0002")
dictList.append(dictData1)
dictList.append(dictData2)

print("리스트 생성 & 할당 --------------------------------------------")
print("dataList1:::",dataList1)
print("dataList2:::",dataList2)
print("dataList3:::",dataList3)
print("dictList:::",dictList)

#리스트가 비었는지 체크
if dataList1:
    print("list Not Empty")
else:
    print("list Is Empty")

print()

#리스트 요소 접근, 할당, 수정, 삭제
print("리스트 접근 --------------------------------------------")
print("list get :::",dataList2[0])
print("list get last :::",dataList2[-1])
print("중복 리스트 요소 접근 :::",dataList3[-1][0])
print("리스트 요수값의 인덱스 번호  :::",dataList2.index(2)) #2가 리스트 몇번째에 있는지
print()

print("리스트 할당 --------------------------------------------")
dataList2.append(4) #리스트 할당 : 맨 마지막 인덱스에 추가 
dataList2.extend([5,6]) #리스트 확장 : 1개 이상 요소를 저할때 사용
dataList2.insert(7,7) #리스트 인텍스 지정해서 할당 : 인덱스,값
print("dataList2 :::",dataList2)
print()

#그외 리스트 메소드  




