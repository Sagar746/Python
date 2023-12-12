import threading


balance = 200

lock = threading.Lock()


def deposit(amount,times,lock):
    global balance
    
    for _ in range(times):
        lock.acquire()
        balance +=amount
        lock.release()

def withdraw(amount,times, lock):
    global balance
    
    for _ in range(times):
        lock.acquire()
        balance -=amount
        lock.release()


deposit_threads = threading.Thread(target=deposit, args=[1,100000, lock])
withdraw_threads = threading.Thread(target=withdraw, args=[1,100000,lock])


deposit_threads.start()
withdraw_threads.start()

deposit_threads.join()
withdraw_threads.join()

print(balance)