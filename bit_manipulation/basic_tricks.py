# SWAP TWO NUMBERS
a = 5
b = 6
print(f"Before: a: {a}, b: {b}")

a = a ^ b
b = a ^ b # (a ^ b) ^ (b) = a
a = a ^ b # (a ^ b) ^ (a==b) = b

print(f"After: a: {a}, b: {b}\n")


# CHECK IF kth BIT IS SET (0-indexed from right to left)
a = 13 # binary: 1 1 0 1 
k = 2 

def isSet(num: int, k: int) -> bool:
    # & with 2 ** k OR (1 << k)

    return num & (1 << k) != 0

print(f"CHECK IF kth bit is SET: ({a}, {k}): {isSet(a, k)}\n")

# SET THE ith BIT
a = 13 
k = 1

def setBit(num: int, k: int) -> int:
    return num | (1 << k)
print(f"SET BIT for ({a}, {k}): {setBit(a, k)}\n")

# TOGGLE THE ith BIT
a = 13
k = 0
def toggleBit(num: int, k: int) -> int:
    return num ^ (1 << k)
print(f"TOGGLE BIT for ({a}, {k}): {toggleBit(a, k)}\n")

# CLEAR THE ith BIT
a = 13
k = 2 
def clearBit(num: int, k: int) -> int:
    return num & ~(1 << k)
print(f"CLEAR BIT for ({a}, {k}): {clearBit(a, k)}\n")


# REMOVE LAST SET BIT
a = 18

def removeLastSetBit(num: int) -> int:
    return num & (num - 1)
print(f"REMOVE LAST SEST BIT for ({a}): {removeLastSetBit(a)}\n")


# CHECK IF POWER OF 2 
a = 4

def isPowerOfTwo(num: int) -> bool:
    if num <= 0: return False
    return num & (num -1) == 0

print(f"IS POWER OF TWO {a}: {isPowerOfTwo(a)}\n")

# CHECK IF NUMBER IS EVEN?
a = 4

def isEven(num: int) -> bool:
    return num & 1 == 0

print(f"IS EVEN {a}: {isEven(a)}\n")

# DIVIDE NUMBER BY 2 and take floor
a = 9

def divideByTwoFloor(num: int) -> int:
    return num >> 1

print(f"DIVIDED BY TWO {a}: {divideByTwoFloor(a)}\n")


# DIVIDE NUMBER BY 2 and take ceil
a = 9

def divideByTwoCeil(num: int) -> int:
    return (num + 1) >> 1

print(f"DIVIDED BY TWO {a}: {divideByTwoCeil(a)}\n")



# ISOLATE RIGHTMOST BIT
a = 13

def isolateRightmostBit(num: int) -> int:
    return num & -num 

print(f"ISOLATE RIGHTMOST BIT {a}: {isolateRightmostBit(a)}\n")

# CHECK IF TWO NUMBERS HAVE OPPOSITE SIGNS
a = 5
b = -3

def haveOppositeSigns(num1: int, num2: int) -> bool:
    return (num1 ^ num2) < 0
print(f"HAVE OPPOSITE SIGNS ({a}, {b}): {haveOppositeSigns(a, b)}\n")

# COUNT NUMBER OF SET BITS
a = 13

def countSetBits(num: int):
    count = 0
    while num:
        count += 1
        num = num & (num -1)
    return count

print(f"COUNT SET BITS ({a}): {countSetBits(a)}\n")




