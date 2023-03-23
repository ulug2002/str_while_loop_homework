def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s = 0
    n = 0
    while s< len(s):
        if s[n].isalpha():
            s+=1
        n += 1
    return n