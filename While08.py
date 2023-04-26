def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0 
    b = 0
    while b < len(s):
        if int(s[b])%2 == 1:
            a += 1 
        b += 1   
    return a
print(main("123456789"))