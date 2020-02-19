def factorial(n):
    # Base Case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)