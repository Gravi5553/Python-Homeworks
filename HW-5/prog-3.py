import time

def time_taken(func, *args):
    start = time.time()
    func(args)
    end = time.time()
    print(end - start)
    
time_taken(sum, 1, 2)