def loop_factorial (num):
    #Start with 1 (0! and 1! are 1)
    ans=1
    # Multiply result looping from 2 to num 
    for i in range (2, num+1):
        ans=ans*i
     #Value of factorial (answer)   
    return ans