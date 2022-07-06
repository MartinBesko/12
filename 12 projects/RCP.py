import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return f"It's a tie computer also guessed {computer}"
    if is_win(user, computer):
        return f'You won! computer guessed {computer}'
    
    return f'You Lost, {computer} is superior'


def is_win(player, oponent):
    if (player == 'r' and oponent == 's') or (player == 's' and oponent == 'p') or (player == 'p' and oponent == 'r'):
        return True

print(play())
