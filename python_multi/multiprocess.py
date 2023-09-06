from multiprocessing import  Process
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

def run():
    p1=Process(target=cpu_bound_task)
    p2=Process(target=cpu_bound_task)
    p3=Process(target=cpu_bound_task)
    # p4=Process(target=cpu_bound_task)
    p1.start()
    p2.start()
    p3.start()
    # p4.start()
    b=time.time()
    print(b-a)
if __name__ =='__main__':
    run() 

# 4.2s