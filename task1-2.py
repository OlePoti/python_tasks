import sys 

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

a = x * 'la-'
b = y * (a[:-1] + ' ')

if z != 0 :
	print ( 'Everybody sing a song: ', (b[:-1] + "!"))
else: print( 'Everybody sing a song:.')
