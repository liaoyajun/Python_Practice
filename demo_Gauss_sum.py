# coding: gbk
# 高斯等差数列求和

first_num = 1
common_difference = 1

count = 0
sum = 0

formula_str = ''

while count < 20:
    sum = sum + first_num +  common_difference * count
    formula_str = formula_str + ' + ' + str(first_num +  common_difference * count)
    count = count + 1

print(formula_str[3:] + ' = ' + str(sum))
