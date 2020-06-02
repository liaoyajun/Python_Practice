# coding: gbk
age = int(input('请输入你的年龄: '))
if age == 0:
    print("你是个婴儿！")
elif age >= 1 and age <= 6:
    print("你是个幼儿！")
elif age >= 7 and age <= 12:
    print("你是个儿童！")
elif age >= 13 and age <= 17:
    print("你是个少年！")
elif age >= 18 and age <= 24:
    print("你是个青年人！")
elif age >= 25 and age <= 64:
    print("你是个中年人！")
else:
    print("你是个老年人！")
