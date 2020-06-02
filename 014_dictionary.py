score = {
   '萧峰': 95,
   '段誉': 97,
   '虚竹': 89
}

print (score['萧峰'])
print(score.get('慕容复'))

score['慕容复'] = 88
print(score.get('慕容复'))

del score['萧峰']
print(score.get('萧峰'))