# coding: gbk
# open('文件名') 打开文件，默认只读
# open('文件名', 'w') 以覆盖写入模式打开
# open('文件名', 'a') 以追加写入模式打开
# file.close() 关闭文件，释放资源

# file.read() 把文件内所有内容读进一个字符串中
# file.readline() 把文件内一行内容读进一个字符串中
# file.readlines() 把文件内所有内容读进一个list中
# 上边三个读取方法，貌似有读取光标，读完一遍，就不会再读

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
