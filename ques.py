#ques 1
a={}
for i in range(int(input("enter key value pairs:"))):
    a[i]=i
n=int(input("enter the value whose key you want to search:"))
flag= False
for key in a.keys():
    if a[key]==n:
        print(key)
        flag=True
        break
if not flag:
 print("key not found")
 #ques 2
student={"pawan":{"hindi":75,"science":85,"maths":70,"punjabi":80},"kamboj":{"hindi":70,"science":80
                                                                            ,"maths":75,"punjabi":78}}
studentName=input("enter name of student:")
if studentName in student:
    print(studentName)
    for key,value in student[studentName].items():
         print(key,value)
else:
    print("student not found")