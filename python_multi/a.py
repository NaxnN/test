def cpu_bound_task():
    """
    模拟cpu密集型任务
    """
    count = 0
    for i in range(50000000):
        count += 1
    return count

import time
a=time.time()
cpu_bound_task()
cpu_bound_task()
cpu_bound_task()
b=time.time()
print(b-a)
# 8.5s