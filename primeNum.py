#Write a python program to check whether given number is prime
#to take input from user      'i' means reminder
num = int(input("enter any number: "))

if num >1:
    for i in range (2,num):
        if num % i== 0:
            print(num,"")
            break
    else:
        print(num,"is a prime number")
elif num == 0 or num == 1 :
    print(num,"is neither prime nor composite number")
