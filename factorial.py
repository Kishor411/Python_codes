#/usr/bin/python3
n = int(input("Enter the number for factorial : "))
factorial = 1
while factorial <= n:
    factorial = factorial*n
    print("Factorial of number",n, "is : ",factorial)
