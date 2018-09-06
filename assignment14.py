                # List comprehension and generator expression
#question number-one
lst=[i**3 for i in range(1,10)]
print(lst)

#question number-two
N=40
list1=[p for p in range(2,N) if 0 not in [p%d for d in range(2,p)]]
print(list1)

#question number-three
#1->memory
#2->speed
                #lambda and map
#question number-one
Celsius=[39.2,36.5,37.3,37.8]
Fahrenheit=list(map(lambda x:(x*(9/5))+32,Celsius))
print(Fahrenheit)

#question number-two
l=[4,5,6,7,8]
l=list(map(lambda x:x**2,l))
print(l)
                #filter and reduce
#question number-one
def isPrime(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
    return flag
l=range(1,100)
primes=list(filter(isPrime,l))
print(primes)

#question number-two
from functools import reduce
l=[1,2,3,4,5]
print(reduce(lambda x,y:x*y,l))