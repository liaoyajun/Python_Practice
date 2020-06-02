# coding: gbk
age = int(input('请输入你的年龄: '))
if age == 0:
    print("你是个婴儿！")
elif 1 <= age <= 6:
    print("你是个幼儿！")
elif 7 <= age <= 12:
    print("你是个儿童！")
elif 13 <= age <= 17:
    print("你是个少年！")
elif 18 <= age <= 24:
    print("你是个青年人！")
elif 25 <= age <= 64:
    print("你是个中年人！")
else:
    print("你是个老年人！")
