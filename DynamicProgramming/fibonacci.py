# iterative fibonacci
# Ot(n)
def fib_it(n):
    if n < 0:
        return "n too small"
    elif n <= 1:
        return n
    else:
        first, second, new = 0, 1, None
        n -= 1
        for _ in range(n):
            new = first + second
            first = second
            second = new
        return new

# print(fib_it(0))

# recursive fibonacci
# this has a terrible time complexity O(2^n)
def fib_rec(n):
    
    # guard
    if n < 0:
        print("n too small")
        return
    
    # base cases
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    return fib_rec(n-1) + fib_rec(n-2)

# recusive fibonacci to list
def fibRecToList(n):
    series = []
    for i in range(n):
        # series.append(fib_rec(i))
        series.append(fib_it(i))
    return series

print(fibRecToList(8))
