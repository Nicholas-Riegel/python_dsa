# Implement a function called, areThereDuplicates which accepts a variable number of arguments, and checks whether there are any duplicates among the arguments passed in.  You can solve this using the frequency counter pattern OR the multiple pointers pattern.

# Restrictions:
# Time - O(n)
# Space - O(n)
# Bonus:
# Time - O(n log n)
# Space - O(1)

# frequency counter solution
def areThereDuplicates1(*args):

    freq = {}

    for item in args:
        freq[item] = freq.get(item, 0) + 1
        if freq[item] > 1:
            return True
    
    return False

# multiple pointers solution
# Ot(n log n), Os(n) can't get to Os(1) in python without passing a list
def areThereDuplicates2(*args):

    sortedArgs = sorted(args)

    for i in range(1, len(sortedArgs)):
        if sortedArgs[i] == sortedArgs[i-1]:
            return True
    
    return False


# print(areThereDuplicates2(1, 2, 3)) # false
# print(areThereDuplicates2(1, 2, 2)) # true 
# print(areThereDuplicates2('a', 'b', 'c', 'a')) # true 

# Frequency Counter - constructNote
# Write a function called constructNote, which accepts two strings, a message and some letters. The function should return true if the message can be built with the letters that you are given, or it should return false.

# Assume that there are only lowercase letters and no space or special characters in both the message and the letters.

# Bonus Constraints:
# If M is the length of message and N is the length of letters:
# Time Complexity: O(M+N)
# Space Complexity: O(N)

def constructNote(model, chars):

    modelFreq, charsFreq = {}, {}

    for char in model:
        modelFreq[char] = modelFreq.get(char, 0) + 1
    
    for char in chars:
        charsFreq[char] = charsFreq.get(char, 0) + 1

    for key in modelFreq:
        if key not in charsFreq or modelFreq[key] > charsFreq[key]:
            return False
        
    return True


# print(constructNote('aa', 'abc')) # false
# print(constructNote('abc', 'dcba')) # true
# print(constructNote('aabbcc', 'bcabcaddff')) # true

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

# print(findAllDuplicates([4,3,2,7,8,2,3,1])) # array with 2 and 3
# print(findAllDuplicates([4, 3, 2, 1, 0])) # []
# print(findAllDuplicates([4, 3, 2, 1, 0, 1, 2, 3])) # array with 3, 2, and 1

# Write a function called sameFrequency. Given two positive integers, find out if the two numbers have the same frequency of digits.

# Your solution MUST have the following complexities:

# Time: O(N)

def sameFrequency(num1, num2):
    
    num1 = str(num1)
    num2 = str(num2)

    freq1, freq2 = {}, {}

    for char in num1:
        freq1[char] = freq1.get(char, 0) + 1
    
    for char in num2:
        freq2[char] = freq2.get(char, 0) + 1
    
    return freq1 == freq2

# print(sameFrequency(182,281)) # true
# print(sameFrequency(34,14)) # false
# print(sameFrequency(3589578, 5879385)) # true
# print(sameFrequency(22,222)) # false