# Input from the user
number = int(input("Enter a number to check if it is prime: "))

# A flag variable to indicate if the number is prime
is_prime = True

# 0 and 1 are not prime numbers
if number <= 1:
    is_prime = False
else:
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
