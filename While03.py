def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0 
    n = 0
    while a < len(s):
        if s[a].isalpha() == False and s[a].isdigit() == False:
            n += 1
        a += 1     
    return n