print('------------------------------------------')
print(range(1,10), type(range(1,10)))
print(list(range(1,10)), type(list(range(1,10))))

print('------------------------------------------')
l = [365, 'everyday', 0.618, True]
print('l')
print(l)

l.append(1024)
print('\nl.append(1024)')
print(l)

del l[0]
print('\ndel l[0]')
print(l)

print('\nl[1:3] 左闭右开，不影响原列表')
print(l[1:3])

sentence = 'I am an English sentence'
sentence_list = sentence.split()
print('''
sentence = 'I am an English sentence'
sentence_list = sentence.split()''')
print(sentence_list)

section = 'Hi. I am the one. Bye.'
section_list = section.split('.')
print('''
section = 'Hi. I am the one. Bye.'
section_list = section.split('.')''')
print(section_list)

fruit_list = ['apple', 'pear', 'orange']
fruit_str = ';'.join(fruit_list)
print('''
fruit_list = ['apple', 'pear', 'orange']
fruit_str = ';'.join(fruit_list)''')
print(fruit_str)

