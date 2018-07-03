#flipping words
import sys
inpt_str = list(sys.argv[1:])
new_str = ''
i=0

while i < len(inpt_str):
    new_str = new_str + ' ' + inpt_str[-1-i]
    i+=1
new_str=new_str.strip()
print(new_str)
