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