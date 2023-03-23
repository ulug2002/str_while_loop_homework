def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a= "salom 2311"
    n = 0
    while n< len(s):
        if s[n].isdigit():
            a += 1
        n += 1
    return s      
