import sys
import mmap

#http://mirrors.apple2.org.za/Apple%20II%20Documentation%20Project/Books/Beneath%20Apple%20DOS.pdf


def dblbytevalue(arr,pos):
	return ord(arr[pos])+ord(arr[pos+1])*256

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
offsetvtoc = 17 * 256 * 16
print len(diskbytes)
print offsetvtoc

if len(diskbytes) > 35 * 256 * 16:
	print "image too large"
	sys.exit(-1)
	


vtoc = diskbytes[offsetvtoc:offsetvtoc+256]

print "*"+repr(vtoc)+"*"
print len(vtoc)

tnr=ord(vtoc[1])
snr=ord(vtoc[2])
print "first catalog track  : %d " % (tnr)
print "first catalog sector : %d " % (snr)

running=0

while tnr != 0:

	track = diskbytes[tnr*256*16+snr*256:tnr*256*16+snr*256+256]

	
	ntnr=ord(track[1])
	nsnr=ord(track[2])

	
#	print "next catalog track  : %d " % (ntnr)
#	print "next catalog sector : %d " % (nsnr)


	for l in range(0,7):
		start = 11+l*35
		end = start + 35
		entry = track[start:end]
	#	print repr(entry)
	#	print "Entry : %d / Start : %d/%d" % (l,start,end)
		ftnr = ord(entry[0])
		fsnr = ord(entry[1])
		
	#	print "Track of file  :%d" % ord(entry[0])
	#	print "Sector of file  :%d" % ord(entry[1])
		type = ord(entry[2])
	#	print "Type of file  :%d" % type 
		fname = entry[3:32]
	#	print "Filename  :%s" % fname
		ename = ""
		for m in fname:
			ename = ename + chr(ord(m) % 128)
	#	print "Filename  :%s" % ename
		
		lo = ord(entry[33])
		hi = ord(entry[34])
	#	print "Length  :%d (%d/%d) => %d" % (lo+hi*256,lo,hi,(lo+hi*256)*256)
		if ftnr!=0 or fsnr !=0:
			print "#%2d: %3d %20s %3d %3d %3d" %(running,type,ename,lo+hi*256,ftnr,fsnr)
			
		if running == anum:
			print "*"
			outfile = open(ename,"wb")
			while ftnr !=0 :
				tsl = diskbytes[ftnr*256*16+fsnr*256:ftnr*256*16+fsnr*256+256]
				ftnr = ord(tsl[1])
				fsnr = ord(tsl[2])
				print ftnr , fsnr
				offset = dblbytevalue(tsl,5)
				print offset
				for sect in range(0,120):
					ctnr = ord(tsl[12 + sect * 2])
					csnr = ord(tsl[13 + sect * 2])
					print ctnr,csnr
					if ctnr == 0 and csnr == 0:
						break
					content = diskbytes[ctnr*256*16+csnr*256:ctnr*256*16+csnr*256+256]
					#print repr(content)
					outfile.write(content)
			outfile.close()
				
				
				
				
		tnr = ntnr
		snr = nsnr
		running=running+1

