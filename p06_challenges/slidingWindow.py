# Sliding Window - maxSubarraySum
# Given an array of integers and a number, write a function called maxSubarraySum, which finds the maximum sum of a subarray with the length of the number passed to the function.

# Note that a subarray must consist of consecutive elements from the original array. In the first example below, [100, 200, 300] is a subarray of the original array, but [100, 300] is not.

# Constraints:
# Time Complexity - O(n)
# Space Complexity - O(1)

# Ot(n) Os(1)
def maxSubarraySum(arr, winSize):

    if len(arr) < 1 or len(arr) < winSize or winSize < 1:
        return None
    
    winVal = sum(arr[:winSize])
    maxVal = winVal

    # i is left index of window
    i = 0
    # j is right index of window
    for j in range(winSize, len(arr)):
            winVal += arr[j]
            winVal -= arr[i]
            if winVal > maxVal:
                maxVal = winVal
            i += 1
        
    return maxVal


# print(maxSubarraySum([100,200,300,400], 2)) #700
# print(maxSubarraySum([1,4,2,10,23,3,1,0,20], 4) ) #39 
# print(maxSubarraySum([-3,4,0,-2,6,-1], 2)) #5
# print(maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2)) #5
# print(maxSubarraySum([2,3], 3)) #null

# Sliding Window - minSubArrayLen
# Write a function called minSubArrayLen which accepts two parameters - an array of positive integers and a positive integer.

# This function should return the minimal length of a contiguous subarray of which the sum is greater than or equal to the integer passed to the function. If there isn't one, return 0 instead.

# Time Complexity - O(n)
# Space Complexity - O(1)
# def minSubArrayLen(arr, n):

#     if len(arr) < 1: return 0

#     start, end = 0, 0
#     total = arr[start]
#     currentLength = None
#     minLength = float('inf')
    
#     while end < len(arr):
        
#         # total = sum(arr[start:end + 1])

#         # print(string(start) + " : " + string(end) + " : total = " + string(total))
    
#         if total >= n:
#             currentLength = end + 1 - start
#             if currentLength < minLength:
#                     minLength = currentLength
#             if start < end:
#                 total -= arr[start]
#                 start += 1
#             else:
#                 end += 1
#                 if end < len(arr):
#                     total += arr[end]
#         else: 
#             end += 1
#             if end < len(arr):
#                 total += arr[end]

#     if minLength < float('inf'):
#         return minLength
        
#     return 0

# Redo with for loop
def minSubArrayLen(arr, n):

    if len(arr) < 1: return 0

    start = 0
    total = 0
    currentLength = None
    minLength = float('inf')
    
    for end in range(len(arr)):
        total += arr[end]
        while total >= n:
            currentLength = end + 1 - start
            if currentLength < minLength:
                minLength = currentLength
            total -= arr[start]
            start += 1
        
    if minLength < float('inf'):
        return minLength

    return 0



# print(minSubArrayLen([2,3,1,2,4,3], 7)) # 2 -> because [4,3] is the smallest subarray
# print(minSubArrayLen([2,1,6,5,4], 9)) # 2 -> because [5,4] is the smallest subarray
# print(minSubArrayLen([4, 3, 1, 8, 1, 2, 3], 11)) # 3
# print(minSubArrayLen([3,1,7,11,2,9,8,21,62,33,19], 52)) # 1 -> because [62] is greater than 52
# print(minSubArrayLen([1,4,16,22,5,7,8,9,10],39)) # 3
# print(minSubArrayLen([1,4,16,22,5,7,8,9,10],55)) # 5
# print(minSubArrayLen([1,4,16,22,5,7,8,9,10],95)) # 0

# Sliding Window - findLongestSubstring
# Write a function called findLongestSubstring, which accepts a string and returns the length of the longest substring with all distinct characters.
# Time Complexity - O(n)
def findLongestSubstring(string):

    longest = 0
    currentLength = 0
    start = 0
    seen = {}

    for end in range(len(string)):

        if string[end] not in seen or seen[string[end]] < start:
            seen[string[end]] = end

        else:
            start = seen[string[end]] + 1          
            seen[string[end]] = end

        currentLength = end + 1 - start
        if currentLength > longest:
            longest = currentLength
    
    return longest

print(findLongestSubstring('')) # 0
print(findLongestSubstring('rithmschool')) # 7
print(findLongestSubstring('thisisawesome')) # 6
print(findLongestSubstring('thecatinthehat')) # 7
print(findLongestSubstring('bbbbbb')) # 1
print(findLongestSubstring('longestsubstring')) # 8
print(findLongestSubstring('thisishowwedoit')) # 6