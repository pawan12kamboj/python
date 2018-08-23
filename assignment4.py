#question number-one
list1=[1,4,5,"pawan","preet","kaur"]
list1.reverse()
print(list1)

#question number-two
str="Hello World"
for i in str:
    if i==i.upper():
        print(i,end="",sep="")

#question number-three
list3=list(map(int,input("enter the elements:").split(",")))
print(*list3)

#question number-four
s=input("enter please")
if s[::-1]==s:
 print("it is palindrome")
else:
 print("it is not palindrome")

#question number-five
list5=[1,2,3]
s=list5
print(list5)
print(s)
print("-"*50)
s[0]="s"
print(list5)
print(s)
print("-"*50)
from copy import deepcopy
list5=[1,2,3]
s=deepcopy(list5)
s[0]="s"
print(list5)
print(s)