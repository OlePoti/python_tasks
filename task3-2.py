#chocolate
import sys
n, m, k = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
if n * m > k and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
