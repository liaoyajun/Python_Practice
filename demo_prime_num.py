# coding: gbk
# ����

range = int(input('��������Ҫ�жϵķ�Χ���ֵ(>1):'))
test_num = 2
prime_str = ''

while test_num <= range:
    # �ж��Ƿ�Ϊ����
    if test_num == 2:
        prime_str = '1-' + str(range) + '�ڵ������У�' + str(test_num)
    else:
        divisor = 2
        flag = True
        while divisor <= (test_num / 2):
            if test_num % divisor == 0:
                print(str(test_num) + '�ܱ�' + str(divisor) + '�����������ж���һ����')
                flag = False
                break
            divisor += 1
        if flag:
            prime_str = prime_str + ' ' + str(test_num)
    test_num += 1

print(prime_str)
