# simple calculator 
#function adds
def add (a , b):
    return a + b

#function substracts
def subtract (a ,b):
    return a - b 

#function multiplies
def multiply (a , b):
    return a * b

#function divides
def divide (a , b):
    return a/b

print ('select oparation.')    
print("1.add")
print("2.substact")
print("3.multiply")
print("4.divide")


#take input from the user
choice = input ("enter choice(1/2/3/4):")

num1 = int(input("enter first number:   "))
num2 = int(input("enter second number:  "))

if choice == "1":
    print (num1+num2)
elif choice == "2":
    print (num1-num2)
elif choice == "3":
    print (num1*num2)
elif choice =="4":
    print (num1/num2)
else :
   print ("invalid input")

