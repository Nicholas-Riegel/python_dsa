# iterative fibonacci
# Ot(n) (this is still the optimal approach)
def fib_iterative(n):

    if n <= 1: 
        return n
    
    first, second, result = 0, 1, None

    for _ in range(n-1):
        result = first + second
        first = second
        second = result

    return second

# recursive fibonacci
# this has a terrible time complexity O(2^n)
def fib_recursive(n):

    if n <= 1: 
        return n
    
    return fib_recursive(n-1) + fib_recursive(n-2)

# memoized recursive fibonacci
# this has time complexity of O(n)
def fib_rec_mem(n, memo={0:0, 1:1}):

    if n in memo:
        return memo[n]
    
    memo[n] = fib_rec_mem(n-1, memo) + fib_rec_mem(n-2, memo)
    
    return memo[n] 

# tabulated fibonacci
# this is "bottom" up dynamic programming
# this returns the fib number at the index
# O(n)
def fib_tabulated(n): 
    
    if n <= 1:
        return n
    
    table = [0, 1]
    
    for _ in range(n-1): 
        table.append(table[-1] + table[-2]) 
    
    return table[n]

# chat's solution
# pre allocates memory so slightly more performant
# O(n)
def fib_tab_chat(n):

    if n <= 1:
        return n
    
    table = [0] * (n + 1)  # ['x'] * 2 => ['x', 'x']
    table[0] = 0
    table[1] = 1
    
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    
    return table[n] 

# fib to list
def fibToList(n): 
    return [fib_iterative(i) for i in range(n)]
    # return [fib_recursive(i) for i in range(n)]
    # return [fib_rec_mem(i) for i in range(n)]
    # return [fib_tabulated(i) for i in range(n)]

print(fibToList(10))
# print(fib_tabulated(3))