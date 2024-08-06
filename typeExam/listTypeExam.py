
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
print("그외 리스트 메소드 --------------------------------------------")
print("List count :::",len(dataList2)) #리스트 요소 갯수
print("List data :::",dataList2.count(7) )#리스트 요소 값 갯수갯수 : 지정된 값이 리스트에 몇개 있는지
print()

delListdata = dataList2.pop(0) #지정한 인덱스의 요소를 삭제하고 삭제된 항목의 값을 반환한다. : 인덱스를 지정하지 않으면 맨 뒤에 값을 삭제
print("deldata :::",delListdata)
print("pop dataList2 :::",dataList2)
print()
dataList2.remove(7) #지정된 값의 리스트 요소를 삭제한다. : 지정된 값이 하나 이상이면 맨 앞에 것만 삭제 된다.
print("remove dataList2 :::",dataList2)

dataList2.reverse()
print("reverse dataList2 :::",dataList2)#리스트 요소값 순서를 뒤집는다. : 정렬X
print()

dataList2.sort() #리스트 정렬
print("리스트 오름차순 정렬 :::",dataList2)
dataList2.sort(reverse=True) #리스트 내림차순 정렬
print("리스트 내림차순 정렬 :::",dataList2)
print()

copyDataList = dataList2.copy() # 리스트 얕은복사
print("리스트 값 Sum :::",sum(copyDataList))  # 리스트 인자 값의 합을 구한다.

condList = [x for x in range(10) if x %2 ==0]