from concurrent.futures import ThreadPoolExecutor
import threading

def task(n):
	print("Processing {}".format(n))
	print("Accessing thread : {}".format(threading.get_ident()))
	print("Thread Executed {}".format(threading.current_thread()))

def main():
	print("Starting ThreadPoolExecutor")
	executor = ThreadPoolExecutor(max_workers=3)
	future = executor.submit(task, (2))
	future = executor.submit(task, (3))
	future = executor.submit(task, (4))
	print("All tasks complete")
  
if __name__ == '__main__':
	main()
