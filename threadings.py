from time import time, sleep
import threading


start_time = time()

def something(id):
    print(f'Going to sleep...{id}')
    sleep(1)
    print(f'Woken up...{id}')


# for i in range(10):
#     print(something(i))

# t1 = threading.Thread(target=something,args=[0])
# t2 = threading.Thread(target=something,args=[1])

# threads = [threading.Thread(target=something, args=[i])for i in range(10)]

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

print(f'End time is {time()-start_time} seconds')


