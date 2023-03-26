def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0 
    n = 0
    while n <len(s):
        if s[n]%2 == 0:
            a += 1
        n += 1    
    return a