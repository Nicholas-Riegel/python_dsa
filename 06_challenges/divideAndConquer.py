# Divide and Conquer - countZeroes
# Given an array of 1s and 0s which has all 1s first followed by all 0s, write a function called countZeroes, which returns the number of zeroes in the array.

# Chat's solution
# def countZeroes(arr):
    
#     if not arr or arr[0] == 0:
#         return len(arr)
    
#     left, right = 0, len(arr) - 1
    
#     while left <= right:

#         mid = (left + right) // 2
        
#         if arr[mid] == 1:
#             left = mid + 1
#         else:  # arr[mid] == 0
#             if mid == 0 or arr[mid - 1] == 1:
#                 return len(arr) - mid
#             right = mid - 1
    
#     return 0  # All ones

# My solution
# Time Complexity - O(log n)
def countZeroes(arr):

    returnNum = 0
    start = 0
    end = len(arr) - 1
    mid = (end + 1 + start) // 2

    if arr[start] == 0:
        return len(arr)
    
    while start < mid:
        
        if arr[mid] == 0 and arr[mid - 1] == 1:
            returnNum = len(arr) - mid
            break
        elif arr[mid] == 0:
            end = mid
        else:
            start = mid
            
        mid = (end + 1 + start) // 2
    
    return returnNum

# print(countZeroes([1,1,1,1,1,1])) # 0
# print(countZeroes([1,1,1,1,1,0])) # 1
# print(countZeroes([1,1,1,1,0,0])) # 2
# print(countZeroes([1,1,1,0,0,0])) # 3
# print(countZeroes([1,1,0,0,0,0])) # 4
# print(countZeroes([1,0,0,0,0,0])) # 5
# print(countZeroes([0,0,0,0,0,0])) # 6


# Divide and Conquer - sortedFrequency
# Given a sorted array and a number, write a function called sortedFrequency that counts the occurrences of the number in the array
# Time Complexity - O(log n)
def sortedFrequency(arr, n):
    
    # Helper function to find first occurrence
    def findFirst(arr, n):
        start = 0
        end = len(arr) - 1
        result = -1
        
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == n:
                result = mid
                end = mid - 1  # Look for earlier occurrence
            elif arr[mid] < n:
                start = mid + 1
            else:
                end = mid - 1
        
        return result
    
    # Helper function to find last occurrence
    def findLast(arr, n):
        start = 0
        end = len(arr) - 1
        result = -1
        
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == n:
                result = mid
                start = mid + 1  # Look for later occurrence
            elif arr[mid] < n:
                start = mid + 1
            else:
                end = mid - 1
        
        return result
    
    first = findFirst(arr, n)
    if first == -1:
        return -1  # Number not found
    
    last = findLast(arr, n)
    return last - first + 1

# print(sortedFrequency([1,1,2,2,2,2,3],2)) # 4 
# print(sortedFrequency([1,1,2,2,2,2,3],3)) # 1 
# print(sortedFrequency([1,1,2,2,2,2,3],1)) # 2 
# print(sortedFrequency([1,1,2,2,2,2,3],4)) # -1

# Divide and Conquer - findRotatedIndex
# Write a function called findRotatedIndex which accepts a rotated array of sorted numbers and an integer. The function should return the index of the integer in the array. If the value is not found, return -1.
# Constraints:
# Time Complexity - O(log n)
# Space Complexity - O(1)
def findRotatedIndex(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Check if left half is sorted
        if arr[left] <= arr[mid]:
            # Target is in left sorted half
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            # Target is in right sorted half
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

print(findRotatedIndex([3,4,1,2],4)) # 1
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8)) # 2
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3)) # 6
print(findRotatedIndex([37,44,66,102,10,22],14)) # -1
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12)) # -1
print(findRotatedIndex([11,12,13,14,15,16,3,5,7,9], 16)) # 5