def sum_of_odd_digits(n):
    total = 0
    for digit in str(n):  # Convert number to string to access each digit
        if int(digit) % 2 == 1:  # Check if the digit is odd
            total += int(digit)
    return total

# Example usage
num = int(input("Enter a number: "))
print("Sum of odd digits:", sum_of_odd_digits(num))


def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    sum_of_powers = sum(int(digit) ** power for digit in num_str)
    return sum_of_powers == num

def armstrong_numbers_in_range(start, end):
    for num in range(start, end + 1):
        if is_armstrong(num):
            print(num, end=" ")

# Example usage
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Armstrong numbers in the range:")
armstrong_numbers_in_range(start, end)


def smallest_prime_digit(n):
    prime_digits = {2, 3, 5, 7}  # Prime numbers from 0-9
    prime_list = [int(digit) for digit in str(n) if int(digit) in prime_digits]
    
    if prime_list:
        return min(prime_list)
    else:
        return "No prime digits found"

# Example usage
num = int(input("Enter a number: "))
print("Smallest prime digit:", smallest_prime_digit(num))
