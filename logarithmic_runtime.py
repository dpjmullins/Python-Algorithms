"""
Code containing logarithmic runtime functions
"""

def LinearSearch(arr1, x):
    """
    Function to find an element in a sorted array
    """
    halfarr = int(len(arr1)/2)
    mid = arr1[halfarr]

    if mid == x:
        return halfarr
    elif x > mid:
        return( LinearSearch(arr1[halfarr:], x) ) ## right side of array
    else:
        return( LinearSearch(arr1[:halfarr], x) ) ## left side of an array
