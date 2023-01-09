import numpy as np
array = np.ones((5, 5))
# заповнити краї
array[1:-1,1:-1] = 0

# def switch(args):
#     for i in args:
#         if i == 1:
#             i = i-1
#             if i == 0:
#                 i = i + 1
#     return i

# new_array = switch(array)
print(array)

print()
# шахмати

Z = np.zeros((8,8), dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)