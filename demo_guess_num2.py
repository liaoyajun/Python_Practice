# coding: gbk
# 猜数字
# 限次数版本

from random import randint
num = randint(1, 100)

# 另一种写法
# import random
# num = random.randint(1, 100)

answer = -1
total_times = 2
count = 0
print('我随机生成了一个 1 - 100 的随机数。你可以猜%d次。' % total_times)


def judge_num(num1, num2):
    if num1 > num2:
        print('你猜的数字大了，答案比' + str(num1) + '小')
    elif num1 < num2:
        print('你猜的数字小了，答案比' + str(num1) + '大')
    else:
        print('恭喜你，猜对了！')


while answer != num:
    if count >= total_times:
        print('抱歉，你输了！')
        break
    else:
        answer = int(input('你猜的数字是：'))
        judge_num(answer, num)
    count += 1
