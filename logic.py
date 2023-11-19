import random


def play_bet(bet, lot):
    win_lot = random.randint(1, 31) # 1, 2, 3, ... , 29, 30
    if lot == win_lot:
        print("Вы выиграли")
        return bet * 2
    else:
        print("Вы проиграли")
        return -bet