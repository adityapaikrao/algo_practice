# XOR From 1 to N — Proof Based on Bit Patterns

We want a closed-form expression for:

```
1 ^ 2 ^ 3 ^ ... ^ N
```

The value of `xor(1 to N)` depends only on the last two bits of `N`, i.e., `N % 4`. The proof comes from examining the binary forms of the last few integers before `N`.

## Understanding xor(1 to N)

Write:

```
N = xxxxxb1b2
```

We use:

```
xor(1 to N) = N ^ xor(1 to N-1)
```

and analyze based on `N % 4`.

# Case 1 — N % 4 == 0

`N = xxxxxx00`

```
xor(1 to N-1) = 0
xor(1 to N)   = N
```

# Case 2 — N % 4 == 1

`N = xxxxx001`

```
xor(1 to N) = (N-1) ^ N
```

Binary:

```
N     = xxxx01
N-1   = xxxx00
xor   = 1
```

So:

```
xor(1 to N) = 1
```

# Case 3 — N % 4 == 2

`N = xxxxx10`

```
xor(1 to N) = (N-2) ^ (N-1) ^ N
```

Binary:

```
N     = xxxx10  
N-1   = xxxx01  
N-2   = xxxx00
```

XOR:

```
xxxx00
^ xxxx01 = xxxx01
^ xxxx10 = xxxx11 = N + 1
```

So:

```
xor(1 to N) = N + 1
```

# Case 4 — N % 4 == 3

`N = xxxxx11`

```
xor(1 to N) = (N-3) ^ (N-2) ^ (N-1) ^ N
```

Binary:

```
N     = xxxx11  
N-1   = xxxx10  
N-2   = xxxx01  
N-3   = xxxx00
```

All bits cancel:

```
xor(1 to N) = 0
```

# Final Result

```
xor(1 to N) =
    N       if N % 4 == 0
    1       if N % 4 == 1
    N + 1   if N % 4 == 2
    0       if N % 4 == 3
```

# XOR of a Range (l to r)

```
xor(l to r) = l ^ (l+1) ^ ... ^ r
xor(1 to l) = 1 ^ 2 ^ ... ^ l
xor(1 to r) = 1 ^ 2 ^ ... ^ l ^ (l+1) ... ^ r
```

Therefore:

```
xor(l to r) = xor(1 to l) ^ xor(1 to r) ^ l
```
