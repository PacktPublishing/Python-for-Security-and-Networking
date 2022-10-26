import threading

def myTask():
    print("Hello World: {}".format(threading.current_thread()))

myFirstThread = threading.Thread(target=myTask)
myFirstThread.start()
