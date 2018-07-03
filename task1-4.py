#!/usr/bin/python
import sys
n = int(sys.argv[1])
i = 0
j = 0
g = 1
fibo = 0
for i in range(0, n-1):
    fibo = g + j
    j = g
    g = fibo
if n==1:
    fibo=1
print(fibo)
