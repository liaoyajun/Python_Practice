# coding: gbk
# range ����ҿ�
for i in range(0, 4):
    print(i)

print('---------------')

for m in range(0, 10):
    for n in range(0, m):
        print('**********'[(9 - n):])
    print()
