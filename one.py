###Python Workshop Day1


##celsius to degrees
"""
while 1:
    
    c = eval(input("Enter temp in celsius"))
    f = c*9/5 + 32
    print(f)
"""
## format
"""
name = (input("Enter your name"))
surname = (input("Enter your surname"))
fathers = (input("Enter your fathers name"))
mothers = (input("Enter your mothers name"))
print(surname+"."+name+"&"+fathers+"@"+mothers)
print(surname+"."+name+"&"+fathers+"@"+mothers,end="!")
"""
##boolean
"""
a=eval(input("Enter a number"))
b=eval(input("Enter a number"))
c=a>b
d=a==b
print(c,d)
print(type(c),type(d))
"""
##if condition
"""
a=eval(input("Enter a number"))
b=eval(input("Enter a number"))
if(a>b):
    print(a,"is greater then",b)
elif(a<b):
    print(b,"is greater then",a)
else:
    print(a,"is equal to",b)
"""
###comparision of 3 numbers
"""
a,b,c=eval(input("Enter 3 numbers"))
if((a>b) and (a>c)):
    print(a,"is greater then",b,"and",c)
elif((b>a) and (b>c)):
    print(b,"is greater then",a,"and",c)
else:
    print(c,"is greater then",a,"and",b)
"""
###calculator
"""
a,b=eval(input("Enter 2 number"))
c=input("Enter an operator amongst +,-,*,/,%")
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)
elif(c=="%"):
    print(a%b)
else:
    print("Wrong operator")
"""
###while condition
"""
count=eval(input("Enter the number of repetitions"))
while count!=0:
    print("HelloWorld")
    count=count-1
"""
###average of 5 numbers
"""
count=5
sum = 0
while count!=0:
    a= eval(input("Enter a number"))
    sum = sum + a
    count = count - 1
print("Average is",sum/5)
"""
###for condition
"""
count=eval(input("Enter the number of repetitions"))
for i in range(count):
    print(i)
"""
###for condition:range
"""
for i in range(0,10,1):
    print(i)
"""
###for condition:string
"""
for letter in "bhairavi sawantdesai":
    print(letter)
"""
###sharing letters
"""
s1="orange"
s2="banana"
for letter in s1:
    if letter in s2:
        print(s1,"and",s2,"share the letter",letter)
"""
###letter slicing
"""
name="N.Gopalkrishnan"
print(name[6])
print(name[-1])
print(len(name))
print(name[:])
print(name[0:])
print(name[:7])
print(name[7:])
print(name[:len(name)])
print(name[1:-1])
"""
###strings
"""
name="N.Gopalkrishnan"
print(name.strip())
print(name.upper())              
print(name.lower())
print(name.find("pal"))
print(name.replace("an","an Sir"))
"""
###list
"""
list = [2,-3,4,-5]
print(list[3])
list[2]=2
list[0]=3
print(list)
list[1],list[3]=eval(input("Enter 2 numbers"))
print(list)
"""
###adding 2 lists
"""
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]          
print(l1+l2)               '''concad'''


for i in range(0,3,1):           ????????
    l3[i]=l1[i]+l2[i]
print(l3)

l1+l2
"""
###is statement
"""
a=[1,3,5,7,9]
b=[0,2,4,6,8]
print(a is b)
"""
###same element list
"""
a=[2,4,6,8]
v=[0]*10
print(v)
"""
###list slicing
"""
a=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
print(a)
print(a[2:-2])
"""
###list slicing
"""
a=["a","b","c","d"]
a[2:5]=["x","y","z"]
print(a)
"""
###list operatins
"""
fruits = ["apple", "banana" , "guava" , "mango", "pineapple"]
fruits.append("papaya")
print(fruits)
fruits.extend(["lichi" , "grapes" , "jackfruit"])
print(fruits)
fruits.insert(2,"orange")
print(fruits)
fruits.pop(2)
print(fruits)
print(fruits.index("guava"))
"""



