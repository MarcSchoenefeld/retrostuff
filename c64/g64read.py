import sys
import os

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def text_to_bits(text):
    """
    >>> text_to_bits("Hi")
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
    """
    bits = bin(int.from_bytes(text.encode(), 'big'))[2:]
    return list(map(int, bits.zfill(8 * ((len(bits) + 7) // 8))))

def text_from_bits(bits):
    """
    >>> text_from_bits([0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1])
    'Hi'
    """
    n = int(''.join(map(str, bits)), 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

	
searchquint=[[0,1,0,1,0],[0,1,0,1,1],[1,0,0,1,0],[1,0,0,1,1],
			[0,1,1,1,0],[0,1,1,1,1],[1,0,1,1,0],[1,0,1,1,1],
			[0,1,0,0,1],[1,1,0,0,1],[1,1,0,1,0],[1,1,0,1,1],
			[0,1,1,0,1],[1,1,1,0,1],[1,1,1,1,0],[1,0,1,0,1]]
			
	
	
nybbles=[[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],
         [1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
		 
		 
def gcr2bytes(thebytes):
	l=tobits(thebytes)
	arr=[]
	for s in range(0,len(l)/5):
		f = l[s*5:s*5+5]
#		print f
		quintfound=False
		for z in range(0,len(searchquint)):
			if searchquint[z]==f:
				quintfound=True
#				print nybbles[z]
				arr.extend(nybbles[z])
				break
		
		if not quintfound:
			print "%s not found" % repr(f)
			
#	print arr
	
	m = frombits(arr)
#	print repr(m) 
	return m
#	return arr
#	sys.exit(0)

g64=sys.argv[1]
print g64
d64=g64.replace("g64","d64")



print d64

#sys.exit(0)


f=open(g64,"rb")

bytes=f.read()


marker=bytes[0:8]
#"GCR-1541"

version=bytes[8]
tracks=ord(bytes[9])

offsetsfull=[0] * tracks
offsetshalf=[0] * tracks


print marker
print version
print tracks

tracknum=1
for i in range(0,tracks/2):
	offset=i*8
	offsetsfull[tracknum]=ord(bytes[12+offset])+ord(bytes[13+offset])*256+ord(bytes[14+offset])*65536+ord(bytes[15+offset])*65536*256
	offsetshalf[tracknum]=ord(bytes[16+offset])+ord(bytes[17+offset])*256+ord(bytes[18+offset])*65536+ord(bytes[19+offset])*65536*256
	print i 
	tracknum=tracknum+1

print "full"
for i in range(0,tracks/2):
	print offsetsfull[i]
	
print "half"
nohalf=True
for i in range(0,tracks/2):
	print offsetshalf[i]
	if offsetshalf[i]!=0:
		nohalf=False

print "half tracks exists: %s" % "no" if nohalf  else "yes"
diskimage=""
endreached=False
secwritten=0
for t in range(0,35):
#for t in range(0,tracks/2):
	if endreached:
		break
	track=t+1
	print "=================================" 
	print "Track: %d" % track
	start=offsetsfull[track]
	print hex(start)
	size=ord(bytes[start])+ord(bytes[start+1])*256
	print size, hex(size)
	data=bytes[start+2:start+2+size]
	#print repr(data)[0:30]
	intrkctr=0
	endofTrack=False
	while intrkctr < size:
		print "seek sector @ %d "  % intrkctr
		print ord(data[intrkctr])
		
		while ord(data[intrkctr])==255:
			intrkctr=intrkctr+1
			if intrkctr >= size:
				endofTrack=True
				print "end of track reached"
				break	
		if endofTrack:
			break
		print "after sync %d " % intrkctr	
		hdr=data[intrkctr:intrkctr+10]
		print "hdr = "+repr(hdr)
		print tobits(hdr)
		hdrclear=gcr2bytes(hdr)
		print "Blk ID: %d " % ord(hdrclear[0])
		print ord(hdrclear[1])
		print "Sect: %d " % ord(hdrclear[2])
		print "Trk:  %d " % ord(hdrclear[3])
		rectrk=ord(hdrclear[3])
		print ord(hdrclear[4])
		print ord(hdrclear[5])
		print ord(hdrclear[6])
		print ord(hdrclear[7])
		hdrgap=data[intrkctr+10:intrkctr+19]
		print "gap=%s" % repr(hdrgap)
		
		intrkctr=intrkctr+19
		print ord(data[intrkctr])
		while ord(data[intrkctr])==255:
				print "sync byte"
				intrkctr=intrkctr+1
		print intrkctr	
		thedata=data[intrkctr:intrkctr+325]
		intrkctr=intrkctr+325
		print repr(thedata)
		cleardata=gcr2bytes(thedata)
		print "thedata=%s" % repr(cleardata)
		print len(cleardata)
		if rectrk==track:
			d64data=cleardata[1:257]
			print "origlen %d" % len(thedata)
			print "written %d" % len(d64data)
			if len(d64data) < 256:
				d64data=d64data.ljust(256)
			diskimage=diskimage+d64data
			secwritten=secwritten+1
		else:
			endreached=True
			break
		while intrkctr < size and ord(data[intrkctr])!=255 :
				print "inter sector gap byte"
				intrkctr=intrkctr+1
	#sys.exit(1)

print "secwritten=%d" % secwritten
	
l = open(d64,"wb")
l.write(diskimage)
l.close()