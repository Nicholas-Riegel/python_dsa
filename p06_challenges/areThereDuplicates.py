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


print(areThereDuplicates2(1, 2, 3)) # false
print(areThereDuplicates2(1, 2, 2)) # true 
print(areThereDuplicates2('a', 'b', 'c', 'a')) # true 
