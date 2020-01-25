import random

def game(r,N):
    #initialises net money to be 0- at the start of function
    net = 0
    for i in range(N):
        #initialises sum to be 0 at the start of each experiment
        sum = 0
        for i in range(4):
            sum += random.randint(1,6)
        if sum < 9:
            net += r
        else:
            net-=1
    print ("this is the net for r = {}: {}".format(r,net))
    if net>0:
        return True
    else:
        return False

#notes: simple to understand problem, should have no issues implementing. Fails test case 3, can be true or false.

print(game(10,100))
print(game(100,100))
print(game(50,50))
print(game(75,75))