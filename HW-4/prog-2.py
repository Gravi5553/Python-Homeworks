def count_frequency(words):
    count = {} 
    for word in words: 
        count[word] = count.get(word, 0) + 1
    return count

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))
 
