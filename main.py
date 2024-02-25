import random


def play():
    user = input('Cual es tu elección? "R" para piedra, "P" para papel, "T" para tijera \n').upper()
    computer = random.choice(["R", "P", "T"])

    if user == computer:
        return "Es un empate"

    if is_winner(user, computer):
        return "Ganaste!"

    return "Perdiste! :("


def is_winner(player, oponent):
    if (player == "R" and oponent == "P") or (player == "T" and oponent == "P") or (player == "P" and oponent == "R"):
        return True


if __name__ == '__main__':
    print(play())
