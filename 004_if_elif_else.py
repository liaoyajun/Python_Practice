# coding: gbk
age = int(input('�������������: '))
if age == 0:
    print("���Ǹ�Ӥ����")
elif 1 <= age <= 6:
    print("���Ǹ��׶���")
elif 7 <= age <= 12:
    print("���Ǹ���ͯ��")
elif 13 <= age <= 17:
    print("���Ǹ����꣡")
elif 18 <= age <= 24:
    print("���Ǹ������ˣ�")
elif 25 <= age <= 64:
    print("���Ǹ������ˣ�")
else:
    print("���Ǹ������ˣ�")

x = int(input('���������: '))
y = int(input('����������: '))
if y >= 0:
    if x >= 0:
        print('�����������ڵ�һ���ޡ�')
    else:
        print('�����������ڵڶ����ޡ�')
else:
    if x < 0:
        print('�����������ڵ������ޡ�')
    else:
        print('�����������ڵ������ޡ�')
