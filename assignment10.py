#question number one
myfile=open('test.txt','r')
a=int(input("enter number of lines you want to read:"))
firstNlines=myfile.readlines()[0:a]
for i in firstNlines:
    print(i)
#question number two
f=open('test.txt','r')
w=(f.read()).split()
count=1
i=0
checklist=[]
for j in range(0,len(w)):
    count=1
    word=w[i]
    if word in checklist:
            pass
    else:
        for l in range(0,len(w)):
            if (i==l):
                pass
            elif (word==w[l]):
                count+=1
        print("Frequency of",word,"is: ",count)
        checklist.append(word)     
    i+=1
f.close()
#question number three
with open("test.txt") as f:
    with open ("python.txt","w+") as f1:
        for line in f:
            f1.write(line)
with open("python.txt") as f1:
    for line in f1:
        print(line)
#question number four
with open('test.txt') as a,open ('python.txt') as b:
    for line1,line2 in zip(a,b):
        print(line1+line2)
#question number five
with open('file1.txt','w') as f:
    for i in range(10):
        number=int(input("Enter any number: "))
        f.write(' %d' % number)
with open('file1.txt', 'r') as f:
    lines=f.readlines()
    for l in lines:
        word=l.split()
    a= [int(i) for i in word]
    a.sort()
    str1 = '\n'.join(str(e) for e in a)
    fout = open('file2.txt','w')
    fout.write(str1)
    fout.close()




