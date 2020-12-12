
def binary_search(start, end, attempt = 1):
    if(start > end):
        return
    
    mid = (start + end)//2
    print("Is it {}? (yes/no)".format(mid), end="")
    answer = input().strip()
    if answer == "yes":
        if(attempt == 1):
            print("Yeey! I got it in 1 try!")
        else:
            print("Yeey! I got it in {} tries!".format(attempt))
        return
    
    else:
        print("Is the number larger than {}? (yes/no)".format(mid), end="")
        answer = input().strip()
        if answer == "yes":
            binary_search(mid + 1, end, attempt + 1)
        
        else:
            binary_search(start, mid - 1, attempt + 1)
        



print("Hi, what is your Name? ", end="")
name = input().strip()
print("Hello {}! Let's play a game!".format(name))
print("Think of random number from 1 to 100, and I'll try to guess it!")
end = "yes"
while end == "yes":
    binary_search(1, 100)
    print("Do you want to play more? ", end="")
    end = input().strip()
print("Bye-bye")