# coding: gbk
# open('�ļ���') ���ļ���Ĭ��ֻ��
# open('�ļ���', 'w') �Ը���д��ģʽ��
# open('�ļ���', 'a') ��׷��д��ģʽ��
# file.close() �ر��ļ����ͷ���Դ

# file.read() ���ļ����������ݶ���һ���ַ�����
# file.readline() ���ļ���һ�����ݶ���һ���ַ�����
# file.readlines() ���ļ����������ݶ���һ��list��
# �ϱ�������ȡ������ò���ж�ȡ��꣬����һ�飬�Ͳ����ٶ�

# file = open('data.txt')
# data1 = file.read()
# data2 = file.readline()
# data3 = file.readlines()
# print(data1, '\n', type(data1))
# print(data2, '\n', type(data2))
# print(data3, '\n', type(data3))
# file.close()

# file = open('data.txt', 'w')
file = open('data.txt', 'a')
file.write("test open('data.txt', 'w')\n")
file.close()
