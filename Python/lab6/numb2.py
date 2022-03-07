# не уверена , но вроде у меня 2 вариант
from threading import Condition, Thread
from queue import Queue

condition = Condition()
q = Queue()


# 1 поток->меняется ключ->2 поток
def function_thread(n):
    while True:
        with condition:
            while q.empty():
                condition.wait()
            try:
                order = q.get_nowait()
                print(f"{n}: {order}")
                if order == "stop":
                    break
            finally:
                print("-----")


Thread(target=function_thread, args=("thread 1",)).start()
Thread(target=function_thread, args=("thread 2",)).start()

for i in range(5):
    q.put(f"order {i}")
for _ in range(2):
    q.put("stop")
with condition:
    condition.notify_all()

