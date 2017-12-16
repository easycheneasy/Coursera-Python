"""
Merge function for 2048 game.
"""
import math

def arraySort(line):
    # iterate each num and move all zero to the end of list
    # this will look like tile to the left
    for index in range(len(line)):
        for line_index in range(len(line)-1):
            if line[line_index] == 0 :
                temp_value = line[line_index]
                line[line_index] = line[line_index + 1]
                line[line_index + 1] = temp_value
    return line

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    line = arraySort(line)
	
    print ("line=")
    print (line)
    # merge the same number to the left
    # iterate each item and merge the same number from the left
    for line_index in range(len(line)-1):
        if line[line_index] != 0 and line[line_index] == line[line_index + 1]:
            line[line_index] += line[line_index + 1]
            line[line_index + 1] = 0
        
        # sort again, move all zero to the right
        # and the merged number should not merge again,
        line = arraySort(line)
 
    
    # return list
    return line

original_line = [0, 16, 16, 8]
print (merge(original_line))
