from concurrent.futures import ThreadPoolExecutor, as_completed
from random import randint
import threading

def execute(name):
	value = randint(0, 1000)
	thread_name = threading.current_thread().name
	print(f'I am {thread_name} and my value is {value}')
	return (thread_name, value)

with ThreadPoolExecutor(max_workers=5) as executor:
	futures = [
		executor.submit(execute,f'T{name}') for name in range(5)
	]
	for future in as_completed(futures):
		name, value = future.result()
		print(f'Thread {name} returned {value}')
