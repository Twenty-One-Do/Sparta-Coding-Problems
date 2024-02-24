import random


def start_up_down_game(a, b):

    while True:
        ans = random.randint(a, b)
        count = 0
        while True:
            inp = int(input("숫자를 입력하세요: "))
            count += 1
            if a <= inp <= b:
                if inp == ans:
                    print("정답입니다!\n시도한 횟수: {}".format(count))
                    break
                else:
                    print('Up' if inp < ans else 'Down')
            else:
                print("유효한 범위를 입력하세요.")

        if input("계속 하시겠습니까(Y/N)?: ") == 'N':
            break


start_up_down_game(1, 100)
