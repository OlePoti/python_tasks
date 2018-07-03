#bank x=many p=percent y=many'
import sys
x = int(sys.argv[1])
p = int(sys.argv[2])
y = int(sys.argv[3])

deposit = x
year = 0
while deposit < y:
    deposit = deposit + (deposit * p * 0.01)
    deposit = round(deposit, 2)
    year += 1
print(year)
