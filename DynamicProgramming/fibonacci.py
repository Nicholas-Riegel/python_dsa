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

# tabulated fibonacci
# this is "bottom" up dynamic programming
# this should return the fib number at the index
# O(n)
def fibTab(n): # 3
    # guard
    if n <= 1:
        return n
    # table list
    table = []
    # populate table list for n+1
    # so that table[n] gives the correct fib number at index of n
    # so f(0)=0, f(1)=1, f(2)=1, f(3)=2
    for i in range(n+1): # [0, 1, 2, 3]
        if i <= 1:
            table.append(i) # [0, 1]
        else:
            table.append(table[-1] + table[-2]) # [0, 1, 1, 2]
    return table[n]

# chat's solution
# pre allocates memory so slightly more performant
# O(n)
def fibTabChat(n):

    if n <= 1:
        return n
    
    table = [0] * (n + 1)  # table[i] = fibonacci number i
    # [0] * 3        # [0, 0, 0]
    # ['x'] * 2      # ['x', 'x']
    table[0] = 0
    table[1] = 1
    
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    
    return table[n]  # Return just the nth fibonacci number

# fib to list
def fibToList(n): 
    # return [fibIt(i) for i in range(n)]
    # return [fibRec(i) for i in range(n)]
    # return [fibRecMem(i) for i in range(n)]
    return [fibTab(i) for i in range(n)]

print(fibToList(10))
print(fibTab(4))