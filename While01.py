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
    while a < len(s):
        if s[n].isdigit():
            n += 1
        a += 1
    return a        