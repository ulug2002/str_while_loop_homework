def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0 
    n = 0 
    while a < len(s):
        if s[a].islower():
            n += 1
        a += 1    
    return n