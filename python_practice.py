#Created By (" M Rabi Khan ")
'''
#Find Average:

numbers = []
sum = 0
totalnum = int(input("Enter the quantity of numbers = "))

for i in range(totalnum):
    val = int(input(f"Plz enter a number {i+1} : "))
    numbers.append(val)
    sum = numbers[i] + sum

avg = sum/totalnum     
print(f"The Average of given numbers = {avg}")   

#--------------------------------------------------------------------

#Program to find Factorial:

factorial = 1
number = int(input("Enter a number to find its Factorial = "))

for i in range(number):
   i = i + 1
   factorial = factorial * i

print(f"\nThe factorial of {number} = {factorial}")    

#--------------------------------------------------------------------

#Get Age Program:

def display():
    val = int(input("Enter your birth year: "))
    curyear = 2023
    val =  curyear - val
    print(f"\nYour Age is {val}")    
display()

#--------------------------------------------------------------

#Find Odd and Even:
val1 = int(input("Plz enter a number: "))
if(val1%2 == 0):
    print("The number is even ")
elif(val1 == 0):
    print("The number is zero")    
else:
    print("The number is odd")    

#---------------------------------------------------------------

#Find Negative and Positive:
val2 = val = int(input("\nPlz enter a number: "))
if(val2 == 0):
    print("The number is zero ")
elif(val2 >= 0):
    print("The number is Positive")    
else:
    print("The number is Negative")    

#---------------------------------------------------------------

#Program To Find Leap Year:

year = int(input("\nEnter a year = "))

if(year%4 == 0):
    print("\nThis is a leap year!")
else:
    print("\nThis is not a leap year!")   

#---------------------------------------------------------------

#Strings methods:  

str = "      Rabi      Khan"
print(str.strip())
print(str.strip())
print("Welcome \n")
values = input("Plz enter num1:")
print("\n"+ values)
fname = "Rabi"
lname = "Khan"
print(f"my name is {fname} {lname}")

#---------------------------------------------------------------

#pop, remove, append, index from List:
list = [("buter","cake","lays"),("1cr","abc","xyz"),(2022,2331,3444)]
list.append(20) #add value at last index
print(list[0])
list = [3,3,8,0,4,5,7,9]
list.pop(6)
#list.remove(8) 
print(list)
list = [23, 45, 74, 11, 21]
#----------------------------------------------------------------------

#List Methods:
l = [4, 10, 2, 9, 7, 6]
print(l)
print(l.index(10))
l.reverse()
print(l)
l.append(15)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.count(2)
print(l)
print(len(l))
print(type(l))

list = [23, 45, 74, 11, 21]
if 74 in list:
    print("Yes it is present")
x = list[1:3]
print(x) 

#----------------------------------------------------------------------

#Match Case
x = int(input("Enter a value for x: "))

match(x):
    case 1:
        print("Hello Case 1")
    case 2:
        print("Hello Case 2")    
    case 3:
        print("Hello Case 3")    
    case 4:
        print("Hello Case 4")    
    case _ if x == 5: #We can create multiple default match case in python
        print("Default Case 1")
    case _ if x  > 6:
        print("Default Case 2")

#----------------------------------------------------------------------

#Tuple In Python
tup = (311, 52, 6, 221, 8, 12)
print(tup)
print(type(tup))
print(len(tup))
print(tup[1])
print(tup[3])
x = tup[1:3]
print(x) 
if 221 in tup:
    print("Yes 221 is present in tuple")

#--------------------------------------------------------------------

#Calculator Program:

def display():
    print("\nEnter 1 for sum")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("\n")

def sum():
        add = num1 + num2
        print(f"The sum = {add}")

def sub():
        subtraction = num1 - num2
        print(f"The subtraction = {subtraction}") 

def mul():
        multi = num1 * num2 
        print(f"The Product = {multi}")   

def div():
        divide = num1 / num2
        print(f"The division = {divide}")    

while(True):
    cont = input("\nDo You want to continue y/n: ")
      
    
    if(cont == "y" or cont == "Y"):    
        display()  
        choice = int(input("Plz enter your choice: "))
        num1 = int(input("Enter number 1 : "))
        num2 = int(input("Enter number 2 : "))

        if(choice == 1):
            sum()
        elif(choice == 2):
            sub()
        elif(choice == 3):
            mul()
        elif(choice == 4):
            div()
        else:
            print("Invalid Input")            
    
    elif(cont == "n" or cont == "N"):
        break
print("\n")

#----------------------------------------------------------------------

#Program that finds Highest & Lowest Marks:

names = []
marks = []   
max = 0
min = 100

student = int(input("Plz enter the number of students = "))

for i in range(student):
    val1 = input(f"\nPlz enter the Name of student {i+1} : ")
    names.append(val1)
    val2 = int(input(f"Plz enter the Marks of student {i+1} : "))
    marks.append(val2) 

for i in range(student):
    if(marks[i] > max):
        max = marks[i]
        x = i

for j in range(student):
    if(marks[j] <= min):
        min = marks[j]
        y = j        

print("\n**********************************")
print(f" Student Got Highest Marks = {names[x]}")
print(f" The highest marks = {max}")
print("**********************************")

print("\n**********************************")
print(f" Student Got Lowest Marks = {names[y]}")
print(f" The Lowest marks = {min}")
print("**********************************")

#---------------------------------------------------------------

#Print Customer Recipt:
'''
products = []
quantity = []
price = []

items = int(input("\nPlz enter the number of items = "))
for i in range(items):
    val1 = input("\nPlz Enter product name: ")
    val2 = int(input("Plz Enter product quantity: "))
    val3 =int(input("Plz Enter product price: ")) 
    products.append(val1)
    quantity.append(val2)
    price.append(val3)
    total = price[i] + total 

print("\n****************************************")
print("* Products \t Quantity \t Price *")
print("****************************************")

for i in range(items):
    print(f"|{products[i]} \t\t |{quantity[i]} \t\t |{price[i]*quantity[i]}")  
print("****************************************")
print(f"*\t   Total Payable Amount = {total}   *")
print("****************************************")
'''
#---------------------------------------------------------------

#Program that shows current time and msg according to time:

import time
import os
timeStamp = time.strftime('%H:%M:%S')
print('The time is: ',timeStamp)

time.sleep(1)
os.system('cls')

timeStamp1 = time.strftime('%H')
print('The time is: ',timeStamp)
timeStamp2 = time.strftime('%M')
print('The time is: ',timeStamp)
timeStamp3 = time.strftime('%S')
print('The time is: ',timeStamp)

if(int(timeStamp1) >= 6 and int(timeStamp1) <= 12):
    print('Good Morning')
    
elif(int(timeStamp1) > 12 and int(timeStamp1) <= 15):
        print('Good After Noon')
else:
    print('Good Night')

'''











