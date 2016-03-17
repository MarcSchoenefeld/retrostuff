import sys
import os
import subprocess

# python parsevsfcpu.py motormania.vsf
# exomizer.exe sfx 49152 glue_motormania.prg froz_motormania.prg -o motor.prg

def getlong(bytes, offset):
	return ord(bytes[offset])+ord(bytes[1+offset])*256+ord(bytes[2+offset])*65536+ord(bytes[3+offset])*65536*256


def getint(bytes, offset):
	return ord(bytes[offset])+ord(bytes[1+offset])*256

def getbyte(bytes, offset):
	return ord(bytes[offset])

	
fname=sys.argv[1]
f=open(fname,"rb")

thefile=f.read()

maincpupos = thefile.find("MAINCPU")+16


#https://github.com/OpenEmu/VICE-Core/blob/master/src/maincpu.c

##else
#    if (0
#        || SMW_DW(m, maincpu_clk) < 0
#        || SMW_B(m, MOS6510_REGS_GET_A(&maincpu_regs)) < 0
#        || SMW_B(m, MOS6510_REGS_GET_X(&maincpu_regs)) < 0
#        || SMW_B(m, MOS6510_REGS_GET_Y(&maincpu_regs)) < 0
#        || SMW_B(m, MOS6510_REGS_GET_SP(&maincpu_regs)) < 0
#        || SMW_W(m, (WORD)MOS6510_REGS_GET_PC(&maincpu_regs)) < 0
#        || SMW_B(m, (BYTE)MOS6510_REGS_GET_STATUS(&maincpu_regs)) < 0
#        || SMW_DW(m, (DWORD)last_opcode_info) < 0)
#        goto fail;
#endif

maj = ord(thefile[maincpupos])
min = ord(thefile[maincpupos+1])

length=getlong(thefile,maincpupos+2)

clk = getlong(thefile,maincpupos+6)
regs_a = ord(thefile[maincpupos+10])
regs_x = ord(thefile[maincpupos+11])
regs_y = ord(thefile[maincpupos+12])
regs_sp = thefile[maincpupos+13]
regs_pc = getint(thefile,maincpupos+14)
regs_status = ord(thefile[maincpupos+16])
lastop = getlong(thefile,maincpupos+17)



print "maj =%d " % maj
print "min =%d " % min

print "clk =%d " % clk
print "regsa = %x " % regs_a
print "regsx = %x " % regs_x
print "regsy = %x " % regs_y

print "regs_sp = %d " % ord(regs_sp)
print "regs_pc = %d (%x) " % (regs_pc,regs_pc)

print "regs_status = %d (%x) " % (regs_status,regs_status)

print "lastop = %d (%x) " % (lastop,lastop)



#  if (SMW_B(m, pport.data) < 0
#        || SMW_B(m, pport.dir) < 0
#        || SMW_B(m, export.exrom) < 0
#        || SMW_B(m, export.game) < 0
#        || SMW_BA(m, mem_ram, C64_RAM_SIZE) < 0
#        || SMW_B(m, pport.data_out) < 0
#        || SMW_B(m, pport.data_read) < 0
#        || SMW_B(m, pport.dir_read) < 0) {

memdump = thefile.find("C64MEM")+16
maj = ord(thefile[memdump])
min = ord(thefile[memdump+1])

length=getlong(thefile,memdump+2)

pport_data = ord(thefile[memdump+6])
pport_dir = ord(thefile[memdump+7])
pport_exrom = ord(thefile[memdump+8])
pport_game = ord(thefile[memdump+9])
ram = thefile[memdump+10:memdump+10+65536]
pport_data_out = ord(thefile[memdump+10+65536])
pport_data_read = ord(thefile[memdump+10+65536+1])
pport_dir_read = ord(thefile[memdump+10+65536+2])

print "maj =%d " % maj
print "min =%d " % min
print "length =%d " % length
print "pport =%d " % pport_data
#pport_data = ord(thefile[memdump+6])


vic2 = thefile.find("VIC-II")+16
maj = ord(thefile[vic2])
min = ord(thefile[vic2+1])
length=getlong(thefile,vic2+2)

allowbadlines = ord(thefile[vic2+6])
badline = ord(thefile[vic2+7])
rasterblank = ord(thefile[vic2+8])
videobuf = thefile[vic2+9:vic2+49]
colorram = thefile[vic2+49:vic2+49+1024]
idlestate = ord(thefile[vic2+49+1024])
lptrig = ord(thefile[vic2+49+1024+1])
lpx = ord(thefile[vic2+49+1024+2])
lpy = ord(thefile[vic2+49+1024+3])
vicbuf=thefile[vic2+49+1024+4:vic2+49+1024+4+40]
sprmask=ord(thefile[vic2+49+1024+4+40])
rambase=getlong(thefile,vic2+49+1024+4+41)
rastercycle=ord(thefile[vic2+49+1024+4+45])
rasterline=ord(thefile[vic2+49+1024+4+46])

vicregs=thefile[vic2+49+1024+4+48:vic2+49+1024+4+112]

pos=vic2+49+1024+4+112

vcregtext=""
lauf=0
for i in vicregs:
	
	if lauf % 16 ==0:
		vcregtext=vcregtext+"\n .byte "
	vcregtext=vcregtext+"$%x" % ord(i)
	if (lauf  % 16) != 15:
		vcregtext=vcregtext+","
	lauf = lauf+1
vcregtext=vcregtext+"0"

sprite_backgrpound_collision=ord(thefile[pos])
dmamask=ord(thefile[pos+1])
sprite_sprite_collision=ord(thefile[pos+2])
vbank_phi1=getint(thefile,pos+3)
mem_counter=getint(thefile,pos+5)
mem_counter_inc=ord(thefile[pos+7])
memptr=getint(thefile,pos+8)
irq_starus=ord(thefile[pos+10])


print "ph1=%x " % vbank_phi1
print "memptr=%x " %memptr

pos=pos+11
for i in range(0,8):
	print "sprr %d = (%d,%d,%d)" % (i, getbyte(thefile,pos+i*3),  getbyte(thefile,pos+i*3+1),getbyte(thefile,pos+i*3+2))

pos=pos+2
	
eventtick=getlong(thefile,pos)
fetch_idx=getbyte(thefile,pos+4)


rambase=getlong(thefile,pos+5)
phi2=getint(thefile,pos+6)
	
print "rambase=%x " % rambase
print "phi2=%x " % phi2

glue = thefile.find("GLUE")+16

print "glue=%x" % glue
print "pos=%x" % (pos+7)
	
memname="mem_"+fname.replace("vsf","mem")
g=open(memname,"wb")
g.write(ram)
g.close()

startadr=0x400
endadr=0x4800
frozen=chr(startadr % 256)+chr(startadr / 256)
frozen=frozen+ram[startadr:endadr]

frozname="froz_"+fname.replace("vsf","prg")

g=open(frozname,"wb")
g.write(frozen)
g.close()



print regs_sp,regs_pc,regs_status,lastop



asname="glue_"+fname.replace("vsf","asm")

g=open(asname,"wb")

l=""".pc = $c000 "Main Program"
sei


ldx #$40
loop:
lda vicregs,x
sta $d000,x
dex 
bpl loop

lda #$3f
sta $dd00

lda #$%x
sta $01
lda #$%x 
ldy #$%x
ldx #$%x

cli 
jmp $%x 

vicregs:
	%s
""" % (pport_data,regs_a,regs_y,regs_x,regs_pc,vcregtext)

g.write(l)
g.close()

cmdline=["kickass.cmd ", asname]
print cmdline




back=subprocess.check_output(cmdline)
print back

