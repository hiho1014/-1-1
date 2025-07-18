#1. 거듭제곱할 숫자를 입력받음
num = input("Enter number: ")

#문자열 메소드로 숫자인지 확인함. 숫자형이면 실수로 변환해주고, 이상한 입력이면 오류메세지.
if num.isnumeric() :
    num = float(num)
else :
    print("Invalid number input.")

#2. 지수를 입력 받음 
exp = input("Enter exponent: ")


# 입력받은 값의 타입이 int가 맞는지 확인함
# int 타입은 문자열 메소드들을 쓸 수 없다고 함. 뒤에 나오는데 왜지
# if type(exp) == int :
if exp.isdecimal() :
    exp = int(exp)
else :
    print("Invalid exponent input.")

root = int(num)
# float(num) 하면 왜인지 모르겠지만 자꾸 str라고 처리함.

for i in range(exp-1):
    root = root * num s

#지피티 추천 코드 깔끔하게 변환:
# root = 1 초기값을 1로 주어야 함.
# for i in range(exp) :
# root = root * num

# &은 문자열만 가능함.
print("Result: ", root)