def reverse_string (string):
    #Initializes empty string
    reversed_str=""
    #Turn over each character to bulid reversed string
    for char in string:
        reversed_str=char+reversed_str
    # Return reversed string   
    return reversed_str    
 