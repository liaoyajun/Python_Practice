# coding: gbk

# Mac encoding='utf-8'
# Windows encoding='gbk'

file = open('scores.txt', encoding='utf-8')
lines = file.readlines()
file.close()

results = []

for line in lines:
    data = line.split()

    sum = 0
    score_list = data[1:]
    for score in score_list:
        point = int(score)
        if point < 60:
            continue
        sum += point
    result = '%s \t: %d\n' % (data[0], sum)
    results.append(result)

output = open('result.txt', 'w', encoding='utf-8')
output.writelines(results)
output.close()
