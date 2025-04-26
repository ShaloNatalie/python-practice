def recursive_factorial(num):
    # Base Case (Factorial of 0 or 1)
    if num==0 or num==1:
        return 1
    # Recursive call (Multiply num by factorial of num-1)
    return num*recursive_factorial(num-1)
