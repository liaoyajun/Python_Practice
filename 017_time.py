import time
start_time = time.time()
print('start:%f' % start_time)
for i in range(10):
    print(i)
time.sleep(2)
end_time = time.time()
print('end:%f' % end_time)
print('total time:%f' % (end_time - start_time))
