# Multiplication table of a given number (up to 20)
def multiplication_table(n):
    print(f"Multiplication Table of {n}:")
    for i in range(1, 21):
        print(f"{n} x {i} = {n * i}")
num = int(input("Enter a number for multiplication table: "))
multiplication_table(num)


# Factorial of a number using a while loop
def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact
num = int(input("Enter a number to calculate its factorial: "))
print(f"Factorial of {num} is {factorial(num)}")

# Numbers from 1 to 100 divisible by both 3 and 5
def divisible_by_3_and_5():
    print("Numbers divisible by both 3 and 5 from 1 to 100:")
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(num, end=" ")
    print()  
divisible_by_3_and_5()
