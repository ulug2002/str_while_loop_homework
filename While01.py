def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    b = 0  
    while a < len(s): 
        if s[a].isdigit():
            b = b +1 
        a = a+1  

        
    return b 
print(main("python 2022"))