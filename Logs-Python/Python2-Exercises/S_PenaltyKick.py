# -*- coding: utf-8 -*-
__author__ = 'Anliven'
from random import choice

score = [0, 0]  # 双方分数
direction = ['left', 'center', 'right']  # 射门方向


def kick():
    print('# Now You Kick! \nPlease choose one side to shoot: left, center, right')
    you = raw_input()
    com = choice(direction)  # random模块的choice方法从一个list中随机挑选一个元素
    if you in direction:  # 射门方向是否正确
        print('You kicked ' + you + ' --- VS --- Computer saved ' + com)
        if you != com:  # 射门方向不一致
            print('Goal!')
            score[0] += 1  # 得1分
        else:
            print('Oops...')
        print('Score: %d(you) - %d(computer)\n' % (score[0], score[1]))
    else:
        print('Error! Exit game!')  # 提示出错并退出
        exit()

    print('Now You Save! \nPlease choose one side to save: left, center, right')
    you = raw_input()
    com = choice(direction)
    print('You saved ' + you + ' --- VS ---  Computer kicked ' + com)
    if you in direction:
        if you == com:
            print('Saved!')
        else:
            print('Oops...')
            score[1] += 1
        print('Score: %d(you) - %d(computer)\n' % (score[0], score[1]))
    else:
        print('Error! Exit game!')
        exit()


times = 0

for times in range(5):  # 点球持续5轮
    print('# Round %d' % (times + 1))
    kick()

while score[0] == score[1]:  # 打破平局
    times += 1
    print('# Round %d' % (times + 1))
    kick()

if score[0] > score[1]:  # 打印最终结果
    print('You Win!')
else:
    print('Computer Win!')
