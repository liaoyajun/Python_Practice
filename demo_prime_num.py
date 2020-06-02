# coding: gbk
# 质数

range = int(input('请输入你要判断的范围最大值(>1):'))
test_num = 2
prime_str = ''

while test_num <= range:
    # 判断是否为质数
    if test_num == 2:
        prime_str = '1-' + str(range) + '内的质数有：' + str(test_num)
    else:
        divisor = 2
        flag = True
        while divisor <= (test_num / 2):
            if test_num % divisor == 0:
                print(str(test_num) + '能被' + str(divisor) + '整除，跳过判断下一个！')
                flag = False
                break
            divisor += 1
        if flag:
            prime_str = prime_str + ' ' + str(test_num)
    test_num += 1

print(prime_str)
