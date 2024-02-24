import random

def start_rock_scissors_paper():
    options = ['가위', '바위', '보']
    winning_set = [['가위', '보'], ['바위', '가위'], ['보', '바위']]
    records = {'win': 0, 'tie': 0, 'lose': 0}
    while True:
        print("-"*30)
        com = random.choice(options)
        me = input('\n가위, 바위, 보 중에 선택: ')
        if me not in options:
            print("\n유효한 입력이 아닙니다.\n")
        else:
            choice = f'\n사용자: {me}\n컴퓨터: {com} \n'
            if me == com:
                print(choice+'비김!\n')
                records['tie'] += 1
            elif [me, com] in winning_set:
                print(choice+'승리!\n')
                records['win'] += 1
            else:
                print(choice+'패배!\n')
                records['lose'] += 1
            if input('다시 하시겠나요?(y/n): ') == 'n':
                break

    print(
        f"\n승리: {records['win']}, 비김: {records['tie']}, 패배: {records['lose']}")

start_rock_scissors_paper()