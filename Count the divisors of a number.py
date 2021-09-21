# Count the divisors of a number
#
#
# Count the number of divisors of a positive integer n.
# 
# Random tests go up to n = 500000.
# 
# Examples:
# divisors(4)  == 3  # 1, 2, 4
# divisors(5)  == 2  # 1, 5
# divisors(12) == 6  # 1, 2, 3, 4, 6, 12
# divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30


def divisors(n):
    div=1
    total=0
    while div<=n:
        if n%div == 0:
            total+=1
        div+=1
    return total


# More code challenges solved in:
# https://github.com/lsfernandez/code_challenges