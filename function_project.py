from curses.ascii import isalnum
def is_palindrome(w):
    """prints information if a given string is a palindrome"""
    w = w.lower().strip() if isalnum else None
    l= len(w)
    if (l < 2): 
       print(True)
    elif w[0] == w[l - 1]:
       return is_palindrome(w[1: l - 1])
    else:
       return False

is_palindrome("Kobyła ma mały bok")