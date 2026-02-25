# MULTIPLE POINTERS
# Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition

# Very efficient for solving problems with minimal space complexity as well

# AN EXAMPLE
# Write a function called sumZero which accepts a sorted array of integers. The function should find the first pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if a pair does not exist

def sumZero(arr):
    
    if len(arr) < 2 or arr[0] >= 0:
        return False
    
    start = 0
    end = len(arr) - 1

    while start < end:
        
        if arr[start] + arr[end] == 0:
            return [arr[start], arr[end]]
        
        elif arr[start] + arr[end] > 0:
            end -= 1
        else:
            start += 1
    
    return False

# print(sumZero([-3,-2,-1,0,1,2,3])) # [-3,3] 
# print(sumZero([-2,0,1,3])) # undefined
# print(sumZero([1,2,3])) # undefined

# countUniqueValues
# Implement a function called countUniqueValues, which accepts a sorted array, and counts the unique values in the array. There can be negative numbers in the array, but it will always be sorted.

# first try
# Ot(n) Os(n) could improve space complexity
def countUniqueValues1(arr):
    unique = set()
    for num in arr:
        unique.add(num)
    return len(unique)

# Ot(n) Os(1)
def countUniqueValues2(arr):

    current = 0
    i = 0
    unique = 0

    if len(arr) > 0:
        unique = 1

    while i < len(arr) - 1:
        i += 1
        if arr[current] != arr[i]:
            unique += 1
            current = i
    
    return unique

# Ot(n) Os(1) but more readable
def countUniqueValues3(arr):

    if len(arr) == 0:
        return 0

    current = 0
    unique = 1

    for i in range(len(arr)):
        if arr[current] != arr[i]:
            unique += 1
            current = i
    
    return unique


print(countUniqueValues3([1,1,1,1,1,2])) # 2
print(countUniqueValues3([1,2,3,4,4,4,7,7,12,12,13])) # 7
print(countUniqueValues3([])) # 0
print(countUniqueValues3([-2,-1,-1,0,1])) # 4
print(countUniqueValues3([1,1,1,1, 2, 2, 2])) # 2
print(countUniqueValues3([2])) # 1