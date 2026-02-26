# SLIDING WINDOW
# This pattern involves creating a window which can either be an array or number from one position to another

# Depending on a certain condition, the window either increases or closes (and a new window is created)

# Very useful for keeping track of a subset of data in an array/string etc.

# An Example
# Write a function called maxSubarraySum which accepts an array of integers and a number called n. The function should calculate the maximum sum of n consecutive elements in the array.

# Ot(n) Os(1)
def maxSubarraySum2(arr, winSize):

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

print(maxSubarraySum2([1,2,5,2,8,1,5],2)) # 10
print(maxSubarraySum2([1,2,5,2,8,1,5],4)) # 17
print(maxSubarraySum2([4,2,1,6],1)) # 6 
print(maxSubarraySum2([4,2,1,6,2],4)) # 13
print(maxSubarraySum2([],4)) # null