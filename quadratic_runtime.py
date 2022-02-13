"""
Code containing quadratic runtime functions
"""

def hasDuplicates(list1):
    """
    Function to find if there duplicate elements in a list
    """

    j = 0
    for i in list1[:-1]:
        for x in list1[j+1:]:
            if i == x:
                return(True)
        j+=1

    return(False)

def BubbleSort( list1 ):
    """
    Function to use the bubble sort method on a list
    """

    len1 = len(list1)

    for i in range(len1):
        
        for j in range(0, len1-i-1):

            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]

    return(list1)