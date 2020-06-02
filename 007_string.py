# 字符串格式化
# 整数 %d 替换
# 浮点数 %f 替换，保留小数位数 %.2f
# 字符串 %s 替换
age = 27
print(age, type(age))
print('My age is %d.' % age)

price = 4.2
print(price, type(price))
print('Price is %.2f.' % price)

date = 'Friday'
print(date, type(date))
print('Today is %s.' % date)

name = 'Lily'
score = 95
print("%s's score is %d." % (name, score))
