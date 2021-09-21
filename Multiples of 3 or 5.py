# Multiples of 3 or 5
#
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).
# 
# Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(number):
    multiplom3=0
    lstm3 = []
    multiplom5 = 0
    lstm5 = []
    contadorm3 = 1
    contadorm5 = 1
    
    while True:
        multiplom3 = 3*contadorm3
        contadorm3 += 1
        if multiplom3 >= number:
            break
        lstm3.append(multiplom3)
        
    while True:
        multiplom5 = 5*contadorm5
        contadorm5 += 1
        if multiplom5 >= number:
            break
        lstm5.append(multiplom5)
    conm3=set(lstm3)
    conm5=set(lstm5)
    listafinal=conm3|conm5
    sumatotal=sum(listafinal)
    return sumatotal


# More code challenges solved in:
# https://github.com/lsfernandez/code_challenges