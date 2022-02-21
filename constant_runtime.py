"""
Code containing constant runtime functions
"""

def isEven(list1, index1):
    """
    This function checks a list of numbers to check if a number in that list is even
    """

    result1 = (list1[index1] % 2) == 0

    return(result1)


def getWordFrequency(dict1, word1):
    """
    This function retrieves a value from a dictionary
    """

    return(dict1[word1])


def findMaxOf2_1(num1, num2):
    """
    Find the maximum of two input numbers and return it

    Method 1 - If else
    """

    if num1 >= num2:
        return(num1)
    else:
        return(num2)


def findMaxOf2_2(num1, num2):
    """
    Find the maximum of two input numbers and return it

    Method 2 - Ternary operator
    """

    return(num1 if num1 >= num2 else num2)


def sumSquare_theorem( n ):
    """
    Return the sum of squares of the first n natural numbers

    Uses the theorem for sum of sqyare of first N natural number
    = (N * (N + 1) * (2*N + 1)) / 6

    n - maximum n
    """

    return(n * (n + 1) * (2 * n + 1) ) // 6
