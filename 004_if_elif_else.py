# coding: gbk
age = int(input('�������������: '))
if age == 0:
    print("���Ǹ�Ӥ����")
elif age >= 1 and age <= 6:
    print("���Ǹ��׶���")
elif age >= 7 and age <= 12:
    print("���Ǹ���ͯ��")
elif age >= 13 and age <= 17:
    print("���Ǹ����꣡")
elif age >= 18 and age <= 24:
    print("���Ǹ������ˣ�")
elif age >= 25 and age <= 64:
    print("���Ǹ������ˣ�")
else:
    print("���Ǹ������ˣ�")
