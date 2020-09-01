################################################################################
##                 Problem 01 : Multiples of 3 or 5                           ##
################################################################################
# If we list all the natural numbers below 10 that are multiples of 3 or 5,    #
# we get 3, 5, 6 and 9. The sum of these multiples is 23.                      #
# Find the sum of all the multiples of 3 or 5 below 1000.                      #
################################################################################

def multiple_of_5(number):
  return number % 5 == 0

def multiple_of_3(number):
  return number % 3 == 0

def main():
    maximum = 1000
    multiples = [x for x in range(2, maximum) if multiple_of_5(x) or multiple_of_3(x)]
    print("The total is {}".format(sum(multiples)))

if __name__ == '__main__':
    main()
