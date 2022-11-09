
import random

print('welcome to rock paper scissors')

first = input('please select rock paper or scissors: ')
rps = ['rock', 'paper', 'scissor']

def answer(first, rps):
    while first == 'rock':
        return random.choice(rps)
    else:
        while first == 'paper':
            return random.choice(rps)
        else:
            while first == 'scissor':
                return random.choice(rps)


print()
print('you chose: ', first, '\ncomputer picked: ', answer(first, rps))
print()