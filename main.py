import list_comprehension as lc
from unittest import main

# Create a list of all the integers from 0 to n-1
print("Create a list of all the integers from 0 to n-1")
print("[x for x in range(n)]")
print(lc.simple_list_range(10))
print("\n")

# Create a list of integer couples from (0,0) to (n - 1,m - 1)
print("Create a list of integer couples from (0,0) to (n - 1,m - 1)")
print("[(x, y) for x in range(n) for y in range(m)]")
print(lc.double_list_comprehension_range(10, 10))
print("\n")

# Random fun with bytes sizes (powers of 2 from 3 to 20)
print("Random fun with bytes sizes (powers of 2 from 3 to 20)")
print("[2 ** n for n in range(3, 20)]")
print(lc.byte_sizes())
print("\n")

# Run unit tests automatically
#main(module='test_module', exit=False)