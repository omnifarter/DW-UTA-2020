import random

def throw_dice(n,nExp):
    count = 0
    for j in range(nExp):
        for i in range(n):
            dice = random.randint(1,6)
            if dice == 6:
                count+=1
                break
    return round(count/nExp,2)


