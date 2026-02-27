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


print(constructNote('aa', 'abc')) # false
print(constructNote('abc', 'dcba')) # true
print(constructNote('aabbcc', 'bcabcaddff')) # true