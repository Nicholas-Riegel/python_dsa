# Divide and Conquer
# This pattern involves dividing a data set into smaller chunks and then repeating a process with a subset of data.

# This pattern can tremendously decrease time complexity

# An Example
# Given a sorted array of integers, write a function called search, that accepts a value and returns the index where the value passed to the function is located. If the value is not found, return -1

def search(arr, n):

    start = 0
    end = len(arr) - 1
    
    while start <= end:

        mid = (start + end) // 2 # // floors it
        
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1

print(search([1,2,3,4,5,6],1)) # 3
print(search([1,2,3,4,5,6],6)) # 5
print(search([1,2,3,4,5,6],11)) # -1