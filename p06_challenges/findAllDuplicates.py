# Frequency Counter - findAllDuplicates
# Given an array of positive integers, some elements appear twice and others appear once. Find all the elements that appear twice in this array. Note that you can return the elements in any order.
# Time Complexity - O(n)

def findAllDuplicates(arr):

    freq = {}
    result = []

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in freq:
        if freq[num] > 1:
            result.append(num)
    
    return result

print(findAllDuplicates([4,3,2,7,8,2,3,1])) # array with 2 and 3
print(findAllDuplicates([4, 3, 2, 1, 0])) # []
print(findAllDuplicates([4, 3, 2, 1, 0, 1, 2, 3])) # array with 3, 2, and 1