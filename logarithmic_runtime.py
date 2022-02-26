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


def find_f_of_x_equal_zero(a, b, input_function, decimalPlace=0):
    """
    DESCRIPTION
    Write an algorithm to calculate the root of a function (i.e. find root such that func(x = root) = 0) given two points, x = a and x = b such that func(x = a) < 0 and func(x = b) > 0

    This is a recursive function to find the value of x in func(x) that returns 0

    VARIABLES
    a               - a number returning f(x) < 0
    b               - a number returning f(x) > 0
    input_function  - is a function with an equation evaluation requiring a single x input and outputting an integer result
    decimalPlace    - The precision of x to search for (increases the time complexity)
    """

    midpoint = (b + a) / 2
    mid_result = input_function(midpoint)

    # Check if midpoint returns f(x) of 0
    # else halve the range and try again
    if round(mid_result, decimalPlace) == 0:
        return(round(midpoint, decimalPlace))

    elif mid_result > 0:
        # search midpoint to a
        return( root_fleshed_out(a, midpoint, input_function, decimalPlace) )
        
    else:
        # search midpoint to b
        return( root_fleshed_out(midpoint, b, input_function, decimalPlace) )