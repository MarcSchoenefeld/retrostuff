import sys
import os

a=sys.argv[1]
print a 
b=sys.argv[2]
c=int(sys.argv[3],0)
print c
d=int(sys.argv[4],0)
print d 
arr = open(a,"rb").read()

e = open(b,"wb")
e.write(chr(c % 256))
e.write(chr(c / 256))
e.write(arr[c:d])
e.close()
