#ques 1
def area_sphere(r):
  return 4*3.14*r*r
radius=int(input("enter radius of sphere:"))
print(area_sphere(radius))
#ques 2
def perfectNumber(n):
      l=[]
      for i in range(1,n):
          if n%i==0:
              l.append(i)
      if sum(l)==n:
            return True
for i in range (1,1001):
    if perfectNumber(i):
        print(i," is a perfect number")
 #ques 3
def printTable(n):
      for i in range(1,11):
        print(n,"x",i,"=",n*i)
n=int(input("enter number:"))
printTable(n)
 #ques 4
def power(base, exp):
  if (exp == 1):
    return (base)
  if (exp != 1):
    return (base * power(base, exp - 1))
base = int(input("Enter base: "))
exp = int(input("Enter exponential value: "))
print("Result:", power(base, exp))
