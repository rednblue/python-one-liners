def simple_list_range(n):
  return [x for x in range(n)]

def double_list_comprehension_range(n, m):
  return [(x, y) for x in range(n) for y in range(m)]

def byte_sizes():
  return [2 ** n for n in range(3, 20)]