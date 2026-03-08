# Divide and Conquer - countZeroes
# Given an array of 1s and 0s which has all 1s first followed by all 0s, write a function called countZeroes, which returns the number of zeroes in the array.
# Time Complexity - O(log n)
def countZeroes(arr):

    numZeroes = 0
    start = 0
    end = len(arr) - 1
    mid = (end + 1 + start) // 2

    if arr[start] == 0:
        return len(arr)
    
    while start < mid:
        
        if arr[mid] == 0 and arr[mid - 1] == 1:
            numZeroes = len(arr) - mid
            break
        elif arr[mid] == 0:
            end = mid
        else:
            start = mid
            
        mid = (end + 1 + start) // 2
    
    return numZeroes

print(countZeroes([1,1,1,1,1,1])) # 0
print(countZeroes([1,1,1,1,1,0])) # 1
print(countZeroes([1,1,1,1,0,0])) # 2
print(countZeroes([1,1,1,0,0,0])) # 3
print(countZeroes([1,1,0,0,0,0])) # 4
print(countZeroes([1,0,0,0,0,0])) # 5
print(countZeroes([0,0,0,0,0,0])) # 6