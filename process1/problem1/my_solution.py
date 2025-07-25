def hello(): 
    print(__name__)
    return "Hello"
a = 1

if __name__ == "__main__":
    print(__name__)
    print(hello())


#원래 거 코드 이상함 고쳐야됨;; 이 파일은 평가자분이 재구현 가능하다고 봐주신 거 
# pip < 파이썬 패키지 설치 함수
#name 이거 없어도 실행은 되긴 하는데 저거는 이 모듈이 메인인지 아닌지 보는 거...