import random

# random.random()方法返回一个随机数，其在0至1的范围之内
print()
print('random.random()')
print(random.random())

# random.uniform()是在指定范围内生成随机数，其有两个参数，一个是范围上限，一个是范围下限
print()
print('random.uniform(2, 6)')
print(random.uniform(2, 6))

# random.randint()是随机生成指定范围内的整数，其有两个参数，一个是范围上限，一个是范围下线
print()
print('random.randint(6, 8)')
print(random.randint(6, 8))

# random.randrange()是在指定范围内，按指定基数递增的集合中获得一个随机数，有三个参数，前两个参数代表范围上限和下限，第三个参数是递增增量
print()
print('random.randrange(6, 28, 3)')
print(random.randrange(6, 28, 3))

# random.choice()是从序列中获取一个随机元素
print()
print('random.choice("www.jb51.net")')
print(random.choice("www.jb51.net"))

# random.shuffle()函数是将一个列表中的元素打乱，随机排序
print()
print('''shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)''')
shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)
print(shuffle_list)

# random.sample()函数是从指定序列中随机获取指定长度的片段，原有序列不会改变，有两个参数，第一个参数代表指定序列，第二个参数是需获取的片段长度
print()
print('random.sample([1, 2, 3, 4, 5], 3)')
print(random.sample([1, 2, 3, 4, 5], 3))
