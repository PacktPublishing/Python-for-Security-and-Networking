import threading

def count(thread_number, **data):
    count = data['count']
    increment = data['increment']
    limit = data['limit']
    while count<=limit:                
        print('Thread:', thread_number, 'count:', count)        
        count+=increment

for thread_number in range(3):
    thread = threading.Thread(target=count, 
                            args=(thread_number,),
                            kwargs={'count':0, 
                                    'increment':1,
                                    'limit':10})
    thread.start()
