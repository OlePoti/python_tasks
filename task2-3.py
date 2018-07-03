#parentheses
import sys
symbol = sys.argv[1]
counter = 0
for i in symbol:
  if i == '(':
      counter += 1
  elif i == ')':
      counter -=1
if counter == 0:
    print ("YES")
else:print ("NO")
