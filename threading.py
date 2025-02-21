import threading,time

def sample1(a):
    for val in range(a):
        print('hello')
        time.sleep(1)

def sample2(b):
    for val in range(b):
        print('bye')
        time.sleep(1)



T1=threading.Thread(target = sample1,args=(5,),name='function1')
T2=threading.Thread(target = sample2,args=(5,),name='function2')

T1.start()
time.sleep(0.2)
T2.start()



T1.join()
T2.join()

print('surprise')

print(T1.is_alive())
print(T2.is_alive())

print(threading.active_count())
print(threading.enumerate())

