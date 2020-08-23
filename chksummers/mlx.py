import sys 
import datetime
import time
import re



def chksum(addr,vals,chk):
    # from https://archive.org/stream/1984-01-computegazette/Compute_Gazette_Issue_07_1984_Jan#page/n185/mode/2up
    tmpchksum = (addr % 256)
    for l in vals:
        tmpchksum = (tmpchksum +  l) % 256
        #print tmpchksum
    return (tmpchksum == chk)

    
    
print chksum(49152,[169, 1, 141, 254, 207, 169],173)
print chksum(49158,[65, 141, 255, 207, 96, 169],171)
#sys.exit(0)
    
    
    
timestr = time.strftime("%Y%m%d-%H%M%S")

fname=sys.argv[1]
try:
    outfile=sys.argv[2]
except:
    outfile="%s.prg" % timestr

print "[+] writing to %s" % outfile
    
    
with open(fname) as f:
    txtcontent = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line

print "[+] autocorrect"

#print txtcontent


txtcontent = [x.strip() for x in txtcontent] 
txtcontent = [x.replace(" ","") for x in txtcontent]
txtcontent = [x.replace("'","") for x in txtcontent]
txtcontent = [x.replace(";",",") for x in txtcontent]
txtcontent = [x.replace("l","1") for x in txtcontent]
txtcontent = [x.replace("O","0") for x in txtcontent]
txtcontent = [x.replace("$","8") for x in txtcontent] # not always but often
txtcontent = [x.replace("S","5") for x in txtcontent] # not always but often
txtcontent = [x.replace("t",",") for x in txtcontent] # not always but often
#txtcontent = [re.sub('[^0-9]:,','', x) for x in txtcontent]

ok = True

startaddr=-1

bytes=""
#print txtcontent

numlines=0
numparsedok=0
lastgok=0
firsterr=0

for p in txtcontent:
    lok=True
    lreason="ok"
    lhead="[ok]"
    #print "[-] testing %s" % p
    (addr,values) = p.split(":")
    addr = int(addr)
    if addr & 1: # odd
        lok = False
        lreason="odd"
    if startaddr==-1:
        startaddr=addr
        expected=addr
    
    if expected != addr:
        lok=False
        lreason="line skipped?"
        
    parseval = values.split(",")
 
    nvalues=[int(s) for s in values.split(",") if s.isdigit()]
    #nval = [int (s) for s in parseval] 
    #values=[x.replace("\d"]
    anz= (len(nvalues) == 7)
    lok=lok and anz    
    if (not anz):
        lreason="num values"
    ok = ok and lok
    chk=False
    if lok:
        chk = chksum(addr,nvalues[0:6],nvalues[6])
        ok = ok and chk
        if chk:
            for l in nvalues[0:6]:
                bytes="%s%s" % (bytes,chr(l))
            #byteline= [chr(p) for p in nvalues[0:6]]
            #bytes="%s%s" % (bytes,byteline)
        else:
            lreason="chk"
            lok=False
            
    
    if not lok:
        lhead = "[!!]"
     
    print lhead,expected,addr , values,"=>" , hex(addr),parseval, "*lok=", lok, "*chk=",chk, "*gok=" , ok, "[%s]" % lreason
    
    
    if ok:
        lastgok=addr
    elif not firsterr:
        firsterr=addr
        break
    expected=expected+6
#print repr(bytes)   

if firsterr!=0 and lastgok !=0:
    print "firsterr: %d" % firsterr 
print "ok until: %d" % lastgok 

if ok:
    f = open(outfile,"wb")
    f.write(chr(startaddr % 256)) # low endian
    f.write(chr(startaddr / 256))
    f.write(bytes)
    f.close()