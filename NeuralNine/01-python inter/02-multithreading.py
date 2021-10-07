import threading 
def function1():
    for x in range(200):
        print("ONE")
def function2():
    for x in range(200):
        print("TWO")
# function1()
# function2()

# Run both functions at the same time
# t1 = threading.Thread(target=function1)
# t2 = threading.Thread(target=function2)
# t1.start()
# t2.start()
def hello():
    for x in range(20):
        print("hello")

t1 = threading.Thread(target=hello)
t1.start()
t1.join()       # join to wait for the thread to finish befor going to the next code
print("bye")