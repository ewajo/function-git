word = ('kajak')
def palindrome(word):
  """prints information if a given word is a palindrome"""
  for letter in word:
    n = int(len(word))
    if n>2:
      for i in range (0,n):
        letter[0] == letter[-1]
        i=i+1
  print(f'{word} is a palindrome')
palindrome(word)