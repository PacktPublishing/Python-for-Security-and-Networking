import threading 
from ThreadWorker import ThreadWorker

def main():
   thread = ThreadWorker()
   thread.start()

if __name__ == "__main__":  
	main()
