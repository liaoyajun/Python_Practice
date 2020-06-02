try:
   file = open('non-exist.txt')
   print ('File opened!')
   file.close()
except:
   print ('File not exists.')
print ('Done')