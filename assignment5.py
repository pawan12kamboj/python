#decision and flow control ques 1
year=int(input("enter the year you want to check"))
if(year%4)==0:
 if(year%100)==0:
     if(year%400)==0:
         print("{0} is a leap year ".format(year))
     else:
         print("{0} is not a leap year ".format(year))
 else:
        print("{0} is a leap year ".format(year))
else:
    print("{0} is not a leap year ".format(year))

#ques 2
l=int(input("enter length"))
b=int(input("enter breadth"))
if l==b:
    print("it is square")
else:
    print("it is rectangle")

#ques 3
a=int(input("enter age of first person"))
b=int(input("enter age of second person"))
c=int(input("enter age of third person"))
if a>b and a>c:
    oldest=a
elif b>a and b>c:
    oldest=b
else:
    oldest=c
    if a<b and a<c:
        youngest=a
    elif b<a and b<c:
        youngest=b
    else:
        youngest=c
print(youngest,oldest)

#ques 4
a=int(input("enter age:"))
sex=input("enter your sex(M or F):").upper()
marital_status=input("enter marital (Y OR N)").upper()
if(sex=="F"):
    print("urban areas")
else:
    if(age>=20 and age<40):
     print("work anywhere")
    elif age>=40 and age<60:
      print("urban areas")
    else:
       print("EEOR")

#QUES 5
a=int(input("enter the quantity"))
cost=100
final_price=0
if a>1000:
 discount=cost*a*0.1
 final_price=(cost*a)-discount
else:
 final_price=cost*a
print(final_price)

#loop
#ques 1
a=input("enter please")
l=[]
for i in range(10):
  l.append(input())
print(l,sep='\n')

#ques 2
while True:
 print("it is infinite loop")