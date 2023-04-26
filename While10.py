def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0 
    b = 0
    while a < len(s):
        c = int(s[a])
        if c % 2== 1:
            b += c
        a += 1
    return b
print(main("1113"))