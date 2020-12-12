from random import randrange

number_of_questions = 8
print("INTEGER DIVISIONS")

for i in range(number_of_questions):
    a = randrange(20)
    b = randrange(1, 10)
    print("{0}/{1}=".format(a, b), end="")
    try:
        c = int(input().strip())
        print("CORRECT!") if (a//b) == c else print("INCORRECT!")
            
    except ValueError:
        print("Please enter Integers Only!")
    


    