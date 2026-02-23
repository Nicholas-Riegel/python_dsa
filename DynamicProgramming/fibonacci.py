# iterative fibonacci
# Ot(n)
def fibIt(n):
    # guard
    if n < 0: 
        return
    # base cases 
    elif n <= 1: 
        return n
    # iteration
    else:
        first, second, new = 0, 1, None
        for _ in range(n-1):
            new = first + second
            first = second
            second = new
        return new

# recursive fibonacci
# this has a terrible time complexity O(2^n)
def fibRec(n):
    # guard
    if n < 0: 
        return
    # base cases
    elif n <= 1: 
        return n
    # recursion
    else: 
        return fibRec(n-1) + fibRec(n-2)

# memoized recursive fibonacci
# this has time complexity of O(n)
def fibRecMem(n, memo={0:0, 1:1}):
    # guard
    if n < 0: 
        return
    # if n is a key in the memo, return the value
    elif n in memo:
        return memo[n]
    # otherwise, memoize and return new result
    else: 
        result = fibRecMem(n-1, memo) + fibRecMem(n-2, memo)
        memo[n] = result
        return result 


# fib to list
def fibToList(n): 
    # return [fibIt(i) for i in range(n)]
    # return [fibRec(i) for i in range(n)]
    return [fibRecMem(i) for i in range(n)]

print(fibToList(45))