# iterative fibonacci
# Ot(n) (this is still the optimal approach)
def fibIt(n):

    if n <= 1: 
        return n
    
    first, second, new = 0, 1, None

    for _ in range(n-1):
        new = first + second
        first = second
        second = new
    
    return new

# recursive fibonacci
# this has a terrible time complexity O(2^n)
def fibRec(n):

    if n <= 1: 
        return n
    
    return fibRec(n-1) + fibRec(n-2)

# memoized recursive fibonacci
# this has time complexity of O(n)
def fibRecMem(n, memo={0:0, 1:1}):

    if n in memo:
        return memo[n]
    
    result = fibRecMem(n-1, memo) + fibRecMem(n-2, memo)
    memo[n] = result
    
    return result 

# tabulated fibonacci
# this is "bottom" up dynamic programming
# this returns the fib number at the index
# O(n)
def fibTab(n): # 3
    
    if n <= 1:
        return n
    
    table = [0, 1]
    
    for _ in range(n-1): # [0, 1] (but it dn matter bc just looping length)
        table.append(table[-1] + table[-2]) # [0, 1, 1, 2]
    
    return table[n] # 2

# chat's solution
# pre allocates memory so slightly more performant
# O(n)
def fibTabChat(n):

    if n <= 1:
        return n
    
    table = [0] * (n + 1)  # ['x'] * 2 => ['x', 'x']
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

print(fibToList(5))
# print(fibTab(3))