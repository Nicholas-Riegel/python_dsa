# iterative fibonacci
# Ot(n)
def fib_it(n):
    if n < 0:
        return "n too small"
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        first, second, new = 0, 1, None
        series = [first, second]
        n -= 2
        for _ in range(n):
            new = first + second
            series.append(new)
            first = second
            second = new
        return series

print(fib_it(5))

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
        series.append(fib_rec(i))
    return series

print(fibRecToList(5))
