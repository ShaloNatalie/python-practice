def sum_of_digits(num):
    # Initialize sum of digits
    total=0
    # Loop through each digit till the number is 0)
    while num>0:
    # Get last digit
        digit=num%10
    # Add it to the total
        total+=digit
    # Drop the last digit    
        num=num//10
    # Return the sum of the digits    
    return total    