def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    n = 0
    while a < len(s):
        if s[a].isalpha():
            n = n + 1
        a = a + 1    
    return n
print(main("samrkand 20031243"))