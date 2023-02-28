def is_palindrome(s):
  """prints information if a given string is a palindrome"""
  s = "".join(s.split()).lower()
  n= len(s)
  if (n <= 1): 
     print(True)
  for i in range (2,n-1):
      if s[0] == s[-1]: 
        return True
      else:
         return False

is_palindrome("Kobyła ma mały bok")