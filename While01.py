def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s = 12345
    n = 0
    while n< len(s):
        if s[n].isdigit():
            s += 1
        n += 1
    print(s)        
    