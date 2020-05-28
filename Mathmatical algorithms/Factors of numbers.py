"""
It is an optimal way of calculating all the factors of the entered number.
"""
def factors(x):
    fact=[]
    for i in range(1,int(sqrt(x))):
        if x%i==0:
            fact.append(i)
            if x//i!=i:
                fact.append(x//i)
    return sorted(fact)



from math import sqrt
print(factors(int(input())))
