# -*- coding: utf-8 -*-
__author__ = 'Anliven'
from random import choice

score = [0, 0]
direction = ['upper-left', 'lower-left', 'center', 'upper-right', 'lower-right']
flag = None


def deco(func):
    def wrapper(*args, **kwargs):
        you = raw_input("## Choose one side(upper-left, lower-left, center, upper-right, lower-right):\n")
        com = choice(direction)
        global flag
        if you in direction:
            if you == com:
                flag = True
            else:
                flag = False
        else:
            print('Error input! Exit game!')
            exit()
        print("## You chose:%s --- vs --- Computer chose:%s" % (you, com))
        func(*args, **kwargs)

    return wrapper


@deco
def kick():
    if flag is False:
        score[0] += 1


@deco
def save():
    if flag is False:
        score[1] += 1


def one_round():
    print('## Now You Kick!')
    kick()
    print('## Now You Save!')
    save()
    print('### Score: (You)%d --- (Computer)%d\n' % (score[0], score[1]))


for times in range(1, 6):
    print('# Round - %d' % times)
    one_round()

times = 5
while score[0] == score[1]:
    times += 1
    print('# Round %d' % times)
    one_round()

if score[0] > score[1]:
    print('You Win!')
else:
    print('Computer Win!')
