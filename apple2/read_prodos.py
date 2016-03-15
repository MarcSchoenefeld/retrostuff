import sys
import mmap

#http://mirrors.apple2.org.za/Apple%20II%20Documentation%20Project/Books/Beneath%20Apple%20DOS.pdf


def dblbytevalue(arr,pos):
	return ord(arr[pos])+ord(arr[pos+1])*256

def getblock(arr,num):
	return arr[num*512:num*512+512]
	
thefile = sys.argv[1]

action="-nothing"
try:
	action= sys.argv[2]
except:
	pass
	
anum=-1
try:
	anum=int(sys.argv[3])
except:
	anum=-1
	
f_diskbytes = open(thefile,"rb")
diskbytes=f_diskbytes.read()
f_diskbytes.close()

p1 = getblock(diskbytes,0)
p2 = getblock(diskbytes,1)
p3 = getblock(diskbytes,2)

print ord(p3[0])
print ord(p3[1])


