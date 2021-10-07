import threading
import time
event = threading.Event()

def my_function():
    print("waiting for the event to trigger...")
    event.wait()
    print("performing action now")

# "y" triggers the event
# t1 = threading.Thread(target=my_function)
# t1.start()
# x = input("do you want to trigger the event? (y/n): ")
# if x == "y":
#     event.set()
# =================== daemon threads =======================
path = "text.txt"
text = ""
def readFile():
    global path, text
    while True:
        with open(path, 'r') as f:
            text = f.read()
        time.sleep(3)

def print_loop():
    for x in range(30):
        print(text)
        time.sleep(1)

# daemon thread keeps reading the thread, so if text.txt is modified and saved, text variable changes too
# when t2 finishes printing the text, deamon thread(t1) finishes too
t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=print_loop)

t1.start()
t2.start()