import queue

numbers = [10, 20, 30, 40, 50, 60, 70]
q = queue.Queue()
for number in numbers:
    q.put(number)

print(q.get())
print(q.get())
print(q.get())
# last in first out
q2 = queue.LifoQueue()
q = queue.Queue()
for number in numbers:
    q2.put(number)

print("last in first out")
print(q2.get())
print(q2.get())
print(q2.get())

# Priority queues
q3 = queue.PriorityQueue()
q3.put((20,"hello world"))
q3.put((1,1))
q3.put((5,7.5))
q3.put((2,True))

print("Priority queues")
while not q3.empty():
    print(q3.get()[1])