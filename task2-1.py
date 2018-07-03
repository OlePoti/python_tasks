import sys
slova = str(sys.argv[1])
n_b_string = slova.replace(" ","")
b = n_b_string.lower()
a = b[::-1]
if b == a:
  print("YES")
else:
  print("NO")
