def bunnyEars2(index):
    if index == 0:
        return 0
    ears = 2 if index%2 == 1 else 3
    return ears + bunnyEars2(index - 1)

assert bunnyEars2(0) == 0
assert bunnyEars2(1) == 2
assert bunnyEars2(5) == 12
    

    