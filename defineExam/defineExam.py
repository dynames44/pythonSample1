#함수에 리턴값이 하나 이상일 수 있다.
def multiReturnDef (str1, str2):
    return str1,str2

returnData = multiReturnDef ("str1", "str2")
print("returnData:::",returnData)
print("type:::",type(returnData)) # 튜플타입으로 리턴된다
print("return[0]:::",returnData[0])
print("return[1]:::",returnData[1])
print()

str1, str2 = multiReturnDef ("str1", "str2") #리턴 변수를 두개로 지정해 각각 받아낸다
print("var1:::",str1)
print("var2:::",str2)
print()

#lambda  함수 : 람다함수의 표현식은 명시하지 않아도 리턴 된다.
#함수명 lambda  = param1, param2 : 표현식
print("lambda::::::::")
add = lambda x, y: x + y
print("lambda add::::::::",add(1,2))