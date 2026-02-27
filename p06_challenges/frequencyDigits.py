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

print(sameFrequency(182,281)) # true
print(sameFrequency(34,14)) # false
print(sameFrequency(3589578, 5879385)) # true
print(sameFrequency(22,222)) # false