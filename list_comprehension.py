def simple_list_range(n):
  return [x for x in range(n)]

def double_list_comprehension_range(n, m):
  return [(x, y) for x in range(n) for y in range(m)]

def byte_sizes():
  return [2 ** n for n in range(3, 20)]

def order_list():
  earners = {'A' : 200000, 'B' : 90000, 'C' : 300000}
  return [(k,v) for v,k in sorted([ (v,k) for k, v in earners.items() if v >= 100000 ], reverse=True)]

def open_file(file_name):
  return [line.strip() for line in open(file_name)]