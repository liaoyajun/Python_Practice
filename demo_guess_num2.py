# coding: gbk
# ������
# �޴����汾

from random import randint
num = randint(1, 100)

# ��һ��д��
# import random
# num = random.randint(1, 100)

answer = -1
total_times = 2
count = 0
print('�����������һ�� 1 - 100 �������������Բ�%d�Ρ�' % total_times)


def judge_num(num1, num2):
    if num1 > num2:
        print('��µ����ִ��ˣ��𰸱�' + str(num1) + 'С')
    elif num1 < num2:
        print('��µ�����С�ˣ��𰸱�' + str(num1) + '��')
    else:
        print('��ϲ�㣬�¶��ˣ�')


while answer != num:
    if count >= total_times:
        print('��Ǹ�������ˣ�')
        break
    else:
        answer = int(input('��µ������ǣ�'))
        judge_num(answer, num)
    count += 1
