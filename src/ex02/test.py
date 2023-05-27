from vector import Vector

vv1 = Vector([[1.0], [2.0], [3.0]])
vv2 = Vector([[4.0], [5.0], [6.0]])
vh1 = Vector([[1.0, 2.0, 3.0]])
vh2 = Vector([[4.0, 5.0, 6.0]])

print('Addition')
print(f'{vv1} + {vv2} = {vv1 + vv2}')
print(f'{vv2} + {vv1} = {vv2 + vv1}')
print(f'{vh1} + {vh2} = {vh1 + vh2}')
print(f'{vh2} + {vh1} = {vh2 + vh1}')

print('Subtraction')
print(f'{vv1} - {vv2} = {vv1 - vv2}')
print(f'{vv2} - {vv1} = {vv2 - vv1}')
print(f'{vh1} - {vh2} = {vh1 - vh2}')
print(f'{vh2} - {vh1} = {vh2 - vh1}')

print('Multiplication')
# Column vector of shape n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(f'{v1} * 5 = {v2}')
# Expected output:
# Vector([[0.0], [5.0], [10.0], [15.0]])

# Row vector of shape 1 * n
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(f'{v1} * 5 = {v2}')
# Expected output
# Vector([[0.0, 5.0, 10.0, 15.0]])

print('Division')
v2 = v1 / 2.0
print(f'{v1} / 2.0 = {v2}')
# Expected output
# Vector([[0.0], [0.5], [1.0], [1.5]])

# Expected output
# ZeroDivisionError: division by zero.
print(f'{v1} / 0.0 = ', end='')
try:
    print(v1 / 0.0)
    print('FAIL: error expected')
except ZeroDivisionError:
    print('ERROR')

# Expected output:
# NotImplementedError: Division of a scalar by a Vector is not defined here.
print(f'2.0 / {v1} = ', end='')
try:
    print(2.0 / v1)
    print('FAIL: error expected')
except NotImplementedError:
    print('ERROR')

print('Shape / Values')
# Column vector of shape (n, 1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
# Expected output
# (4,1)

print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
# Expected output
# [[0.0], [1.0], [2.0], [3.0]]

# Row vector of shape (1, n)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
# Expected output
# (1,4)

print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
# Expected output
# [[0.0, 1.0, 2.0, 3.0]]

print('Transpose')
# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(f'{v1} shape = {v1.shape}')
# Expected output:
# (4,1)

print(f'T({v1}) = {v1.T()}')
# Expected output:
# Vector([[0.0, 1.0, 2.0, 3.0]])

print(f'T({v1}) shape = {v1.T().shape}')
# Expected output:
# (1,4)

# Example 2:
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(f'{v2} shape = {v2.shape}')
# Expected output:
# (1,4)

# Expected output:
# Vector([[0.0], [1.0], [2.0], [3.0]])
print(f'v2={v2}')
print(f'T({v2}) = {v2.T()}')

# Expected output:
# (4,1)
print(f'T({v2}) shape = {v2.T().shape}')

print('Dot product')
# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
# 18.0

v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(f'{v3} dot {v4} = {v3.dot(v4)}')
# Expected output:
# 13.0

print('str & repr')
print(f'__repr__ = {v1.__repr__()}')
# Expected output: to see what __repr__() should do
# [[0.0, 1.0, 2.0, 3.0]]

print(v1)
# Expected output: to see what __str__() should do
# [[0.0, 1.0, 2.0, 3.0]]

print()
print('--- 01.02.00 ---')
print(Vector([[1., 2e-3, 3.14, 5.]]).values)
print()
print('--- 01.02.01 ---')
print(Vector(4).values)
print()
print('--- 01.02.02 ---')
try:
    Vector(-1)
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.03 ---')
print(Vector((10, 12)).values)
print()
print('--- 01.02.04 ---')
try:
    print(Vector((3, 1)).values)
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.05 ---')
try:
    v = Vector((1, 1))
    print(v.values)
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.06 ---')
try:
    Vector((4, 7.1))
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.07 ---')
v = Vector(4)
print(v.values)
print()
print('--- 01.02.08 ---')
print(v * 4)
print()
print('--- 01.02.09 ---')
print(4.0 * v)
print()
print('--- 01.02.10 ---')
try:
    v * 'hi'
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.11 ---')
v = Vector(4)
v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
print((v + v2).values)
print()
print('--- 01.02.12 ---')
try:
    v + Vector([0.0, 0.0, 0.0, 0.0])
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.13 ---')
try:
    v + 'hello'
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.14 ---')
try:
    v + None
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.15 ---')
print((v - v2).values != (v2 - v).values)
print()
print('--- 01.02.16 ---')
print(Vector(4) / 2)
print()
print('--- 01.02.17 ---')
print(Vector(4) / 3.14)
print()
print('--- 01.02.18 ---')
try:
    Vector(4) / 0
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.19 ---')
try:
    Vector(4)/ None
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.20 ---')
try:
    None / Vector(4)
except Exception as ex:
    print(f'  ERROR: {ex}')
print()
print('--- 01.02.21 ---')
try:
    3 / Vector(3)
except Exception as ex:
    print(f'  ERROR: {ex}')
