"""
Merge function for 2048 game.
"""

def array_sort(arrline):
    """ 
    Function to move all non-zero number to its left.
    """
    #iterate each num and move all zero to the end of list
    #this will look like tile to the left
    for dummy_index in range(len(arrline)):
        for line_index in range(len(arrline)-1):
            if arrline[line_index] == 0 :
                temp_value = arrline[line_index]
                arrline[line_index] = arrline[line_index + 1]
                arrline[line_index + 1] = temp_value
    return arrline

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    newline = list(line)
    newline = array_sort(newline)
    
    # merge the same number to the left
    # iterate each item and merge the same number from the left
    for line_index in range(len(newline)-1):
        if newline[line_index] != 0 and newline[line_index] == newline[line_index + 1]:
            newline[line_index] += newline[line_index + 1]
            newline[line_index + 1] = 0
        # sort again, move all zero to the right
        # and the merged number should not merge again,
            newline = array_sort(newline) 
            
    # return list
    return newline

