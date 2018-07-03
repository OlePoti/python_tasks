#biletik
import sys
a_1 = int(sys.argv[1])
a_2 = int(sys.argv[2])
S = ""

bilet = 0

for x in range(a_1,a_2+1):
    if len(str(x)) < 6:
        S = "0"*(6-len(str(x))) + str(x)
    else:
        S = str(x)
    if int(S[0])+int(S[1])+int(S[2])==int(S[3])+int(S[4])+int(S[5]):
            bilet += 1
print(bilet)
