###seconds to HH:MM:SS
"""
ss=eval(input("Enter the time in seconds"))
hh= ss//3600
ss_new= ss%3600
mm= ss_new//60
mm_new= ss%60
ss= mm_new%60
print(hh,":",mm,":",ss)
"""
###vowels
"""
s="My name is bhairavi"
i=0
for letter in s:
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u" :
        i=i+1
print(i)
"""
###details of students
"""
n=eval(input("Enter the number of students"))
print("Sr. No.\tName\tRoll No")
i=1                                         ///better if used in file
while n!=0:
    name=input("Enter name")
    roll=eval(input("Enter roll number"))
    print(i,"\t",name,"\t",roll)
    i=i+1
    n=n-1
"""
###grades
"""
n=eval(input("Enter your percentage"))
if n>=90:
    print("O")
elif 80<=n<=89:
    print("A")
elif 70<=n<=79:
    print("B")
elif 60<=n<=69:
    print("C")
elif 50<=n<=59:
    print("D")
elif 40<=n<=49:
    print("E")
elif n<=39:
    print("F")
else:
    print("Invalid")
"""
###counting translator
"""
translator={}
translator={"one":"ek","two":"do","three":"teen"}
n=(input("Enter the english number"))
print(translator[n])
"""
###opening and reading a file
"""
filepath="D:\\TEXT.txt"
file=open(filepath, 'r')
'''read to the file'''
lines=file.readlines()
print(lines)
print(type(lines))
'''print(lines.splitlines())'''
file.close()
"""
###writing on a file
"""
filepath="D:\\TEXT.txt"
file=open(filepath, 'a')
file.write("HELLO WORLD")
file.close()

file=open(filepath, 'r')
lines=file.read()
print(lines)
file.close()
"""
###
"""
filepath="D:\\TEXT.txt"
file=open(filepath,'a')
new_content=["\n","bhairavi ","vijay ","sawantdesai"]
file.writelines(new_content)
file.close()

file=open(filepath, 'r')
#lines=file.read()         splitlines??????
lines=file.readlines()
print(lines.splitlines)
file.close()
"""
###define
"""
def printmyname():
    print("My name is Bhairavi")
printmyname()
"""
###compare
"""
def compare(a,b):
    if a>b:
        print(a," is greater then",b)
    elif b>a:
        print(b," is greater then",a)
    else:
        print(a," is equal to",b)
compare(10,20)
"""
###default parameter
"""
def printmyname(count=5):
    for i in range(count):
        print("My name is Bhairavi")
printmyname(10)
printmyname()
"""
###global and local variable
"""
def increment(x):
    print("Beginning execution of increment, x=",x)
    x=x+1
    print("Ending execution of increment, x=",x)
    return x

def main():
    x=5                    
    print("Before increment, x=",x)
    x=increment(x)
    print("After increment, x=",x)
global x
x=5
main()
"""
###dictionary
"""
fruits={}
print(fruits)

fruits={"a":"apple","b":"banana","c":"custard apple"}
print(fruits)

fruits["d"]="dragon fruit"
print(fruits)

print(fruits["c"])
print(fruits["b"])

fruits_new={1:"mango",2:"watermelon",3:"fruits_new1"}
fruits_new1 = {"I":"muskmelon","II":"papaya","III":"grapes"}
fruits["fruits_new1"]=fruits_new1
fruits.update(fruits_new)
print(fruits)
print(fruits["fruits_new1"]["II"])
"""
###





















































