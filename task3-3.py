#lost card
import sys
n = int(sys.argv[1])
cards = str(sys.argv[2:])

for i in range(1,n+1):
    if str(i) not in cards:
        lost = str(i)
print(lost)
