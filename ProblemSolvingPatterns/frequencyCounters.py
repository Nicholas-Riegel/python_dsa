# FREQUENCY COUNTERS
# This pattern uses objects or sets to collect values/frequencies of values

# This can often avoid the need for nested loops or O(N^2) operations with arrays / strings
# Write a function called same, which accepts two arrays. The function should return true if every value in the array has it's corresponding value squared in the second array. The frequency of values must be the same.

def same1(arr1, arr2):

    if len(arr1) != len(arr2):
        return False
    
    freq1, freq2 = {}, {}
    
    for num in arr1:
        num = num * num
        if num in freq1:
            freq1[num] += 1
        else:
            freq1[num] = 1

    for num in arr2:
        if num in freq2:
            freq2[num] += 1
        else:
            freq2[num] = 1

    return freq1 == freq2

def same2(arr1, arr2):

    if len(arr1) != len(arr2):
        return False
    
    freq1, freq2 = {}, {}
    
    for num in arr1:
        num = num * num
        freq1[num] = freq1.get(num, 0) + 1
    for num in arr2:
        freq2[num] = freq2.get(num, 0) + 1
    
    return freq1 == freq2




print(same2([1, 2, 3], [4, 1, 9]))  # True
print(same2([1, 2, 3], [1, 9]))  # False  
print(same2([1, 2, 1], [4, 4, 1]))  # False