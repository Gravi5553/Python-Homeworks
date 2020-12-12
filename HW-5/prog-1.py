def my_range(start, stop, step = 1):
    if step > 0 and start < stop:
        while start < stop:
            yield start
            start += step
    elif step < 0 and start > stop:
        while start > stop:
            yield start
            start += step
    
for i in my_range(0, 5):
    print(i)
    
    

    