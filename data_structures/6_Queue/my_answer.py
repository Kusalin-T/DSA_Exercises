from collections import deque
import threading as th
import time

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)    
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
    def front(self):
        return self.buffer[-1]
    
orderqueue=Queue()
def place_orders(orders):
    for order in orders:
        print(f'Placing order for: {order}')
        orderqueue.enqueue(order)
        time.sleep(0.5)

def serve_orders():
    time.sleep(1)
    while True:
        if orderqueue.size()<=0:
            print('ALL SERVED')
            break
        print(f'Serving: {orderqueue.dequeue()}')
        time.sleep(2)


orders = ['pizza','samosa','pasta','biryani','burger']
producer = th.Thread(target=place_orders, args=(orders,))
consumer = th.Thread(target=serve_orders)
#producer.start()
#consumer.start()


def print_binary(n):
    qqq=Queue()
    qqq.enqueue('1')
    for _ in range(n):
        front = str(qqq.front())
        print(front)
        qqq.enqueue(front + "0")
        qqq.enqueue(front + "1")

        qqq.dequeue()

print_binary(10)