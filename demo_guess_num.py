# coding: gbk
# 猜数字
# 不限次数版本

from random import randint
num = randint(1, 100)

# 另一种写法
# import random
# num = random.randint(1, 100)

print('我随机生成了一个 1 - 100 的随机数。')
answer = -1
while answer != num:
    answer = int(input('你猜的数字是：'))
    if answer > num:
        print('你猜的数字大了，答案比' + str(answer) + '小')
    elif answer < num:
        print('你猜的数字小了，答案比' + str(answer) + '大')
    else:
        print('恭喜你，猜对了！')
