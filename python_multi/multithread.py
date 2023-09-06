import threading
import time
a=time.time()
def cpu_bound_task():
    """
    模拟cpu密集型任务
    """
    count = 0
    for i in range(50000000):
        count += 1
    print(count)
    print(time.time()-a)
    return count


t1=threading.Thread(target=cpu_bound_task)
t2=threading.Thread(target=cpu_bound_task)
t3=threading.Thread(target=cpu_bound_task)
t1.start()
t2.start()
t3.start()
b=time.time()
print(b-a)
# 7s