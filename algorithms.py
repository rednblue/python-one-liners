def is_anagram(x1, x2):
  return lambda x1, x2 : sorted(x1) == sorted(x2)

def is_palyndrome(x1, x2):
  return lambda x1, x2 : x1 == x2[::-1]

def permutations(n):
  factorial = lambda n : n * factorial (n-1) if n > 1 else 1
  return factorial(n)