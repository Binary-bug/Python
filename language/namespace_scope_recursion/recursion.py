def fact(n):
    """Calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2 , n + 1):
            result *=f
    return result


#recursive factorial

def factorial(n):
    """Calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


for i in range(130):
    print(i,factorial(i))



def fib(n):
    """F(n) = F(n-1) + F(n-2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibiter(n):
    if n==0:
        result = 0
    elif n==1:
        result = 1
    else:
        temp1 = 1
        temp2 = 0
        for f in range(1,n):
            result = temp1 + temp2
            temp2 = temp1
            temp1 = result
    return result


for i in range(36):
    print(i,fibiter(i))