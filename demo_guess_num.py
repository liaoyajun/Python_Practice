# coding: gbk
# ������
# ���޴����汾

from random import randint
num = randint(1, 100)

# ��һ��д��
# import random
# num = random.randint(1, 100)

print('�����������һ�� 1 - 100 ���������')
answer = -1
while answer != num:
    answer = int(input('��µ������ǣ�'))
    if answer > num:
        print('��µ����ִ��ˣ��𰸱�' + str(answer) + 'С')
    elif answer < num:
        print('��µ�����С�ˣ��𰸱�' + str(answer) + '��')
    else:
        print('��ϲ�㣬�¶��ˣ�')
