#lists
#question number-one
a = input('Enter a value: ')
b = input('Enter a value: ')
c = input('Enter a value: ')
d = input('Enter a value: ')
e = input('Enter a value: ')
f = input('Enter a value: ')
g = input('Enter a value: ')
h = input('Enter a value: ')
i = input('Enter a value: ')
j = input('Enter a value: ')
list1 = [a, b, c, d, e, f, g, h, i, j]
print(list1)

#question number-two
list2=list1+['google','apple','facebook','microsoft','tesla']
print(list2)

#question number-three
list3=[1,2,3,1,5,1,5,6,1]
print(list3.count(1))

#question number-four
list4=[1,7,8,3,6,9]
list4.sort()
print(list4)

#question number-five
a=[1,8,16,4,5,2]
b=[6,3,7,12,11,10]
c=a+b
c=sorted(c)
print(c)

#question number-six
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

#tuples
#question number-one
x = ("pawanpreet")
y = reversed(x)
print(tuple(y))
A= (5, 10, 15, 20)
B= reversed(A)
print(tuple(B))

#question number-two
t=(1,2,3,4,5)
print("the max is:" ,max(t))
print("the min is:" ,min(t))

#strings
#question number-one
str="hello my name is pawan"
str1=str.upper()
print(str1)

#question number-two
str2="123456"
print(str2.isnumeric())

#question number-three
str3="Hello World"
str4=str3.replace("World","pawan")
print(str4)