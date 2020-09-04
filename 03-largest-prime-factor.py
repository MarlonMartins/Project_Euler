################################################################################
##                 Problem 03: Largest prime factor                           ##
################################################################################
# The prime factors of 13195 are 5, 7, 13 and 29.                              #
# What is the largest prime factor of the number 600851475143 ?                #
################################################################################

################################################################################
import math

def generate_prime_factors(number):
    prime_factors = []

    # Divide by the first prime number (2), while it's possible
    while (number % 2 == 0):
        prime_factors.append(2)
        number = number / 2

    # Since 2 it's the only even number that is prime, we can look now only for
    # odd numbers. This way we can go from 3 to the square root of the number
    # requested
    square_root = int(math.sqrt(number))
    for factor in range(3, square_root + 1, 2):
        while (number % factor == 0):
            prime_factors.append(factor)
            number = number / factor

    # If number is a prime number greater than 2
    if number > 2:
        prime_factors.append(number)
    print(prime_factors)
    return prime_factors

def find_largest_number(numbers):
    return max(numbers)

def main():
    requested_number = 600851475143
    prime_factors = generate_prime_factors(requested_number)
    print(find_largest_number(prime_factors))

if __name__ == '__main__':
    main()
