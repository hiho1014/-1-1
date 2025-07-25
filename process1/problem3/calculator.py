
#리스트 형태로 실수 2개와 연산자 동시에 입력 받을 수 없나?
#input("실수 2개와 연산자를 입력해주세요.", a, c, b)
#tuple("input")

if __name__ == "__main__":
    a = input("첫번째 실수를 입력")

# 여기서 invalid number input 처리

#이렇게 하면 숫자 검증 방식이 틀림. 이 메소드는 정수 양수만 가능
# if a.isnumeric() :
#     a = float(a)
# else :
#     print("Invalid number input.")

try:
    a = float(a)
except ValueError:
    print("Invalid number input.")
    exit()


b = input("두번째 실수를 입력")

# 여기서 invalid number input 처리


try:
    b = float(b)
except ValueError:
    print("Invalid number input.")
    exit()



# if b.isnumeric() :
#     b = float(b)
# else:
#     print("Invalid number input.")



#if c != in [+, -, *, /] :
#    print("Invalid operator.")

#str랑 함수랑 매칭하는 법 없나? 리스트로...



#헉 이것들 내장함수 아니래 

def add(a, b) :
    return a + b
def subtract(a, b) :
    return a - b
def multiply(a, b) :
    return a * b
def divide(a, b) :
     if b == 0:
        print("Error: Division by zero.")
        exit()
        return a / b


c = input("+, -, *, / 중에 하나를 입력하세요.")

#mapping 변수 지정해서 딕셔너리 사용

map = {"+":add, "-":subtract, "*":multiply, "/" : divide}


if c in map :
    func = map[c]
    result = func(a,b)
    print("Result:", result)
else:
    print("Invalid operator.")



# 간단하게 하려면 역시 다중이프인가... 라고 시도해봤음
#if c == "+" : 
#    w = add(a,b)
#elif c == "-" : 
#    w = subtract(a, b) 
#elif c == "*" : 
#    w = multiply(a, b) 
#elif c == "/" : 
#    w = divide(a, b)

#print("Result: ", w)




#map이라는 사전 안에 c라는 요소들이 있다면, func는 map 안에서 그 c의 키워드에 대응되는 거임. 





# 틀린 것
#    print(result)
#    print(func(a,b))

#또는
#print(f"Result: {func(a, b)}")