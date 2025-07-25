import math

def is_number(value):
    try:
        num = float(value)
        return math.isfinite(num)
    except ValueError:
        return False
    
def is_int(value):
    try:
        num = int(value)
        return True
    except ValueError:
        return False

def main():
    #1. 거듭제곱할 숫자를 입력받음
    num = input("Enter number: ")
    
    if not is_number(num):
        print("Invalid number input.")
        return
    num = float(num)

    #2. 지수를 입력 받음 
    exp = input("Enter exponent: ")
    if not is_int(exp):
        print("Invalid exponent input.")
        return
    exp = int(exp)

    root = num
    for i in range(abs(exp)-1):
        root = root * num

    if exp == 0:
        root = 1;
    if exp < 0:
        root = 1 / root

    

#지피티 추천 코드 깔끔하게 변환:
# root = 1 초기값을 1로 주어야 함.
# for i in range(exp) :
# root = root * num

# &은 문자열만 가능함.
    print("Result: ", root)

if __name__ == '__main__':
    main()