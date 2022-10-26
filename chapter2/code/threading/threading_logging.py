import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] - %(threadName)-10s : %(message)s')

def thread(name):
    logging.debug('Starting Thread '+ name)
    time.sleep(5)
    print("%s: %s" % (name, time.ctime(time.time())))
    logging.debug('Stopping Thread '+ name)

def check_state(thread):
	if thread.is_alive():
		print(f'Thread {thread.name} is alive.')
	else:
		print(f'Thread {thread.name} it not alive.')
		  
th1 = threading.Thread(target=thread, args=('MyThread',))
th2 = threading.Thread(target=thread, args=('MyThread2',))
th1.setDaemon(True)
th1.start()
th2.start()

check_state(th1)
check_state(th2)

while(th1.is_alive()):
	logging.debug('Thread is executing...')
	time.sleep(1)
	
th1.join()
th2.join()
