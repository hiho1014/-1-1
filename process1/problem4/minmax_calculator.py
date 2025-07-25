def main():
    try:
        user_input = input("임의의 숫자를 공백으로 구분하여 입력하세요: ")

        if ' ' not in user_input:
            print("공백을 넣어 숫자를 구분해주세요.")
            return

        list_n = list(map(float, user_input.split()))

        if len(list_n) < 2:
            print("최소 두 개 이상의 숫자를 입력해주세요.")
            return
        
        # 입력을 받아 공백 기준으로 나누고 float으로 변환
        #아래의 코드는 공백 없이 쳤을 때 처리 못함
        # list_n = list(map(float, input("임의의 숫자를 공백으로 구분하여 입력하세요: ").split()))

        # if ' ' not in list_n:
        #     print("공백을 넣어 숫자를 구분해주세요.")
        #     return

        # 아래의 코드 문법 틀림
        # if list_n for IndexError : 
        # print("공백을 입력해주세요")
        
        # 리스트를 오름차순 정렬 (min이 맨 앞, max가 맨 뒤로 감)
        list_n.sort()

        # pop으로 최소값(맨 앞), 최대값(맨 뒤) 꺼냄. pop은 큐 자료구조에 적합. 리스트도 큐긴 함. 
        min_val = list_n.pop(0)
        max_val = list_n.pop(-1)

        # 이렇게도 된다고 함. pop으로 하는 것보다 이게 더 간편하고 빠른건가?
        # min_val = list_n[0]
        # max_val = list_n[-1]

        print(f"Min: {min_val}, Max: {max_val}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
