"""
Code containing linear runtime functions
"""

def getMin( list1 ):
    """
    Function to find the minimum number element in an array
    """

    min1 = list1[0]

    for i in list1[1:]:

        if i < min1:

            min1 = i

    return(min1)


def findMax( list1 ):
    """
    Function to find the maximum number in an unsorted array
    """
    max1 = 0 
    counter = 0

    for i in list1:

        counter+=1

        if i > max1:

            max1 = i

    return(max1)


def sumList( list1 ):
    """
    Function to find the sum of an array
    """

    ## Initialise a variable to hold the sum
    sumOfList = 0

    for i in list1:
        ## increment sum variable
        sumOfList += i

    return(sumOfList)

def sumSquare( n ):
    """
    Return the sum of squares of the first n natural numbers

    n - maximum n
    """

    output1 = 0

    for i in range(1,n+1):
        output1 += (i*i)

    return(output1)
    
