class Animal:
    def __init__(self, name):
        self.name = name;
        self.clues = {
            "elephant": ["I have exceptional memory", "I am the largest land-living mammal in the world", "I can't jump"],
            "tiger": ["I am the biggest cat", "I come in black and white or orange and black", "I live for about 25 years"],
            "bat": ["I use echo-location", "I can fly", "I see well in dark"]
        }
        
    def __get_clues(self):
        return self.clues[self.name]
        
    def guess_who_am_i(self):
        print("I will give you 3 hints, guess what animal I am\n")
        
        for clue in self.__get_clues():
            print(clue)
            print("Who am I?:", end="")
            answer = input().strip()
            if(answer.lower() == self.name.lower()):
                print("You got it! I am " + self.name + "\n\n")
                return
            else:
                print("Nope, try again!\n")
        
        print("I'm out of hints! The answer is: " + self.name + "\n\n")
            

e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
            