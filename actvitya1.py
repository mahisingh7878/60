#Take a number input from the user and check if it is prime

from math import sqrt


number=int(input("enter a number ")) #4 15


for i in range(2,int(sqrt(number))+1): #@ tu  2+1=3 2 to 3+1=4
    if number%i==0: #15%3  =0

        flag=True
        break
    
if flag:
    print(number,"it is not a prime number ")
        

else:
        print(number,"it is a prime number ")

