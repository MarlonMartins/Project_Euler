################################################################################
##                 Problem 01 : Multiples of 3 or 5                           ##
################################################################################
# If we list all the natural numbers below 10 that are multiples of 3 or 5,    #
# we get 3, 5, 6 and 9. The sum of these multiples is 23.                      #
# Find the sum of all the multiples of 3 or 5 below 1000.                      #
################################################################################
################################################################################
# FIRST APPROACH: This solution works fine, as long as the number is small, eg.
# 1000000. If we use numbers like 1000000000, it will take a lot of time or even
# result in an error.

import time
'''
def is_multiple_of(number, choice):
  return number % choice == 0

def main():
    maximum = 1000000000
    start = time.time()
    multiples = [x for x in range(2, maximum) if is_multiple_of(x,5) or is_multiple_of(x,3)]
    print("The total is {}".format(sum(multiples)))
    print("Finished in {} seconds".format(time.time()-start))

'''

################################################################################
# SECOND APPROACH: This solution is more efficient, calculating the sum of the
# numbers less than "choice" that are divisible by 3, plus the sum of the numbers
# less than "choice" that are divisible by 5 fine, minus the numbers divisible by
# 15, since they are duplicated.

def sum_divisible_by(n):
  maximum = 1000000
  p = maximum // n
  return n*(p*(p+1)) // 2

def main():
    start = time.time()
    total  = sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)
    print("The total is {}".format(total))
    print("Finished in {} seconds".format(time.time()-start))

if __name__ == '__main__':
    main()
