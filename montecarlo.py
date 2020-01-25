
import random
def pi_approx_monte_carlo(n):
    count = 0
    in_circle = 0
    while(in_circle<n):
        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)
        if x**2 + y**2  <= 1.0:
            in_circle+=1
            count+=1
        else: count+=1
    return round(4*in_circle/count,2)

#issues it doesn't pass vocareum
print(pi_approx_monte_carlo (100))
print(pi_approx_monte_carlo (100000))
print(pi_approx_monte_carlo (10000000))

