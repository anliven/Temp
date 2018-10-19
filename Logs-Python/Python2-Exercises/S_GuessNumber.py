# -*- coding: utf-8 -*-
# 声明当前文件使用utf-8编码，以便显示中文字符，也可写成“# coding=utf-8”或“# coding:utf-8”，默认使用ascii码

from random import randint  # 导入随机数模块

name = raw_input('请输入姓名: ')  # raw_input()将所有输入作为字符串看待并返回字符串类型
f = open('S_GuessNumber.txt', 'r')
lines = f.readlines()  # 分行读取文件内容并赋值给相关变量
f.close()

# 初始化一个空字典scores,并定义相关的键和值
scores = {}  #
for l in lines:
    s = l.split()  # 每一行数据拆分成list
    scores[s[0]] = s[1:]  # 第一项作为字典的key,剩下的作为value

# 查找当前玩家数据,如果没找到,初始化数据
score = scores.get(name)  # 字典的get()方法按照key寻找对应项，如果不存在返回空值None
if score is None:
    score = [0, 0, 0]
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
print("历史记录: 已经玩了%d 次，最少%d 轮猜出答案" % (game_times, min_times))


def GuessNumber(num1, num2):  # 定义比较函数
    if num1 > num2:
        print("too big! please try again!")
        return False
    elif num1 < num2:
        print("too small! please try again!")
        return False
    else:
        print("BingGo!")
        return True


r_number = randint(1, 100)  # 获取随机数
times = 0  # 单次游戏尝试轮数

print("Please input your number: ")
bing = False
while bing is False:
    t_number = input()
    if t_number < 0 or t_number > 100:
        print("Wrong number! Exit game")
        break
    times += 1
    bing = GuessNumber(t_number, r_number)
print("本次游戏尝试轮数: %d" % times)

game_times += 1  # 游戏次数
if times < min_times or min_times == 0:
    min_times = times  # 单次最少尝试轮数
total_times = total_times + times  # 总尝试轮数
if game_times > 0:
    avg_times = float(total_times) / game_times  # 平均每次尝试轮数
else:
    avg_times = 0
print("已经玩了%d 次，最少%d 轮猜出答案，平均%.2f 轮猜出答案" % (game_times, min_times, avg_times))

scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'  # !
    result += line
f = open('S_GuessNumber.txt', 'w')
f.write(result)  # 将结果写入文件
f.close()

# 代码说明 - “line = n + ' ' + ' '.join(scores[n]) + '\n'”
#  n          --- 字典的键
#  ' '        --- 空格隔开
#  scores[n]  --- 字典的值
#  ' '.join(scores[n]) --- 以空格将字典的值连接起来
#  '\n'       --- 换行
