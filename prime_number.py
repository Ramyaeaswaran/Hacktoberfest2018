#python program to check whether the entered value is prime or not
#Author- Ramya Easwaran	
num = int(input("enter a number: "))
 for i in range(2, int(num/2)):
    if num % i  == 0:
        print("not prime number")
        break
else:
    print("prime number")
