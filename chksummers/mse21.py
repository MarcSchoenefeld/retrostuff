#MSE 2.1

"""
0fc6  A0 00       LDY #$00           - A:20 X:ff Y:0e SP:f5   -B   C
0fc8  A5 14       LDA $14            - A:20 X:ff Y:00 SP:f5   -B  ZC
0fca  85 3D       STA $3D            - A:4b X:ff Y:00 SP:f5   -B   C
0fcc  B1 14       LDA ($14),Y        - A:4b X:ff Y:00 SP:f5   -B   C
0fce  18          CLC                - A:00 X:ff Y:00 SP:f5   -B  ZC
0fcf  65 3D       ADC $3D            - A:00 X:ff Y:00 SP:f5   -B  Z
0fd1  0A          ASL A              - A:4b X:ff Y:00 SP:f5   -B
0fd2  69 00       ADC #$00           - A:96 X:ff Y:00 SP:f5 N -B
0fd4  85 3D       STA $3D            - A:96 X:ff Y:00 SP:f5 N -B
0fd6  C8          INY                - A:96 X:ff Y:00 SP:f5 N -B
0fd7  C0 0F       CPY #$0F           - A:96 X:ff Y:01 SP:f5   -B
0fd9  D0 F1       BNE $0FCC          - A:96 X:ff Y:01 SP:f5 N -B


0fcc  B1 14       LDA ($14),Y        - A:69 X:ff Y:0d SP:f5 N -B
0fce  18          CLC                - A:00 X:ff Y:0d SP:f5   -B  Z
0fcf  65 3D       ADC $3D            - A:00 X:ff Y:0d SP:f5   -B  Z
0fd1  0A          ASL A              - A:69 X:ff Y:0d SP:f5   -B
0fd2  69 00       ADC #$00           - A:d2 X:ff Y:0d SP:f5 N -B
0fd4  85 3D       STA $3D            - A:d2 X:ff Y:0d SP:f5 N -B
0fd6  C8          INY                - A:d2 X:ff Y:0d SP:f5 N -B
0fd7  C0 0F       CPY #$0F           - A:d2 X:ff Y:0e SP:f5   -B
0fd9  D0 F1       BNE $0FCC          - A:d2 X:ff Y:0e SP:f5 N -B
0fcc  B1 14       LDA ($14),Y        - A:d2 X:ff Y:0e SP:f5 N -B
0fce  18          CLC                - A:00 X:ff Y:0e SP:f5   -B  Z
0fcf  65 3D       ADC $3D            - A:00 X:ff Y:0e SP:f5   -B  Z
0fd1  0A          ASL A              - A:d2 X:ff Y:0e SP:f5 N -B
0fd2  69 00       ADC #$00           - A:a4 X:ff Y:0e SP:f5 N -B   C
0fd4  85 3D       STA $3D            - A:a5 X:ff Y:0e SP:f5 N -B
0fd6  C8          INY                - A:a5 X:ff Y:0e SP:f5 N -B
0fd7  C0 0F       CPY #$0F           - A:a5 X:ff Y:0f SP:f5   -B
0fd9  D0 F1       BNE $0FCC          - A:a5 X:ff Y:0f SP:f5   -B  ZC

0fdb  60          RTS                - A:a5 X:ff Y:0f SP:f5   -B  ZC


0f77  85 39       STA $39            - A:a5 X:ff Y:0f SP:f7   -B  ZC
0f79  A9 00       LDA #$00           - A:a5 X:ff Y:0f SP:f7   -B  ZC
0f7b  A0 03       LDY #$03           - A:00 X:ff Y:0f SP:f7   -B  ZC
0f7d  46 39       LSR $39            - A:00 X:ff Y:03 SP:f7   -B   C
0f7f  2A          ROL A              - A:00 X:ff Y:03 SP:f7   -B   C
0f80  88          DEY                - A:01 X:ff Y:03 SP:f7   -B


0f77  85 39       STA $39            - A:b4 X:ff Y:0f SP:f7   -B  ZC
0f79  A9 00       LDA #$00           - A:b4 X:ff Y:0f SP:f7   -B  ZC
0f7b  A0 03       LDY #$03           - A:00 X:ff Y:0f SP:f7   -B  ZC
0f7d  46 39       LSR $39            - A:00 X:ff Y:03 SP:f7   -B   C
0f7f  2A          ROL A              - A:00 X:ff Y:03 SP:f7   -B
0f80  88          DEY                - A:00 X:ff Y:03 SP:f7   -B  Z
0f81  D0 FA       BNE $0F7D          - A:00 X:ff Y:02 SP:f7   -B
0f7d  46 39       LSR $39            - A:00 X:ff Y:02 SP:f7   -B
0f7f  2A          ROL A              - A:00 X:ff Y:02 SP:f7   -B
0f80  88          DEY                - A:00 X:ff Y:02 SP:f7   -B  Z
0f81  D0 FA       BNE $0F7D          - A:00 X:ff Y:01 SP:f7   -B
0f7d  46 39       LSR $39            - A:00 X:ff Y:01 SP:f7   -B
0f7f  2A          ROL A              - A:00 X:ff Y:01 SP:f7   -B   C
0f80  88          DEY                - A:01 X:ff Y:01 SP:f7   -B
0f81  D0 FA       BNE $0F7D          - A:01 X:ff Y:00 SP:f7   -B  Z
0f83  20 88 0F    JSR $0F88          - A:01 X:ff Y:00 SP:f7   -B  Z
0f88  29 1F       AND #$1F           - A:01 X:ff Y:00 SP:f5   -B  Z
0f8a  09 40       ORA #$40           - A:01 X:ff Y:00 SP:f5   -B
0f8c  C9 40       CMP #$40           - A:41 X:ff Y:00 SP:f5   -B
0f8e  D0 02       BNE $0F92          - A:41 X:ff Y:00 SP:f5   -B   C
0f92  C9 5B       CMP #$5B           - A:41 X:ff Y:00 SP:f5   -B   C
0f94  90 02       BCC $0F98          - A:41 X:ff Y:00 SP:f5 N -B




>C:1c4b  00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00

"""


chars='7abcdefghijklmnopqrstuvwxyz23456'

bytes00=[0x00,0x38,0x7e,0x7f,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff]
bytes4b=[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

bytes96=[0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff]


def asc2val(str):
    r = -1 
    try:
        r = chars.find(str)
    except:
        pass
    return r

#def asc5tobytes4(str):
#    fullbits = ""
#    for i in str:
#        fullbits = fullbits +  


def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


def chars8tobytes5(str):
    ges = 0
    for l in str:
        lz = asc2val(l)
        ges = ges * 32 + lz
    #    print ges

    base=2**64
    return bytes(base+ges)#[-7:]


def line24tobytes15(str):
    ges = ""
    ges = ges + chars8tobytes5(str[0:8])
    ges = ges + chars8tobytes5(str[8:16])
    ges = ges + chars8tobytes5(str[16:24])
    return ges
    

    
    
    
def mse21(start,thebytes):

    #print "*",thebytes,"*"

    acc = start % 256

    loc3d = acc

    yreg = 00            # y-index

    for yreg in range (0,15):

        acc = thebytes[yreg]

        cf = 0               # carry

        acc = acc + loc3d
        
        if (acc > 255):
            cf = 1
            acc = acc % 256

        acc = acc + acc # + cf 

#       print "nach asl %s", hex (acc)
        cf = 0
        if acc > 255:
            cf = 1
            acc = acc % 256
            
        acc = acc + cf

        if acc > 255:
            cf = 1
            acc = acc % 256
            
        loc3d=acc
        
#       print "loc3d =  %s acc   =  %s  " % (hex(loc3d),hex(acc))

#    print loc3d

    """
    0f77  85 39       STA $39            - A:b4 X:ff Y:0f SP:f7   -B  ZC
    0f79  A9 00       LDA #$00           - A:b4 X:ff Y:0f SP:f7   -B  ZC
    0f7b  A0 03       LDY #$03           - A:00 X:ff Y:0f SP:f7   -B  ZC
    * 0f7d  46 39       LSR $39            - A:00 X:ff Y:03 SP:f7   -B   C
    0f7f  2A          ROL A              - A:00 X:ff Y:03 SP:f7   -B
    0f80  88          DEY                - A:00 X:ff Y:03 SP:f7   -B  Z
    0f81  D0 FA       BNE $0F7D          - A:00 X:ff Y:02 SP:f7   -B

    """


    loc39 = acc

    y= 3
    acc = 0
    while y > 0: 
        cf = loc39 % 2
        loc39 = int(loc39 / 2)
        acc = acc + acc + cf
        if acc > 255:
            acc = acc - 256
            cf = 1
        #print "y = %d, loc39 =  %s acc   =  %s  cf=%d  " % (y,hex(loc39),hex(acc),cf)

        y = y - 1
        
        
    ret =  chars[acc]+chars[loc39]    
    return ret
    

    
# v2.0 

"""
.C:0fc6  A0 0E       LDY #$0E
.C:0fc8  A5 14       LDA $14
.C:0fca  45 15       EOR $15
.C:0fcc  85 3D       STA $3D
.C:0fce  B1 14       LDA ($14),Y
.C:0fd0  18          CLC
.C:0fd1  65 3D       ADC $3D
.C:0fd3  0A          ASL A
.C:0fd4  69 00       ADC #$00
.C:0fd6  85 3D       STA $3D
.C:0fd8  88          DEY
.C:0fd9  10 F3       BPL $0FCE
.C:0fdb  60          RTS"""    
    
def mse20(start,thebytes):

    #print "*",thebytes,"*"

    acc = (start % 256) ^ int (start / 256)

    loc3d = acc

    yreg = 14            # y-index

    while yreg >= 0:
#    for yreg in range (0,15):

        acc = thebytes[yreg]

        cf = 0               # carry

        acc = acc + loc3d
        
        if (acc > 255):
            cf = 1
            acc = acc % 256

        acc = acc + acc # + cf 

#       print "nach asl %s", hex (acc)
        cf = 0
        if acc > 255:
            cf = 1
            acc = acc % 256
            
        acc = acc + cf

        if acc > 255:
            cf = 1
            acc = acc % 256
            
        loc3d=acc
 
        yreg = yreg - 1
#       print "loc3d =  %s acc   =  %s  " % (hex(loc3d),hex(acc))

#    print loc3d

    """
    0f77  85 39       STA $39            - A:b4 X:ff Y:0f SP:f7   -B  ZC
    0f79  A9 00       LDA #$00           - A:b4 X:ff Y:0f SP:f7   -B  ZC
    0f7b  A0 03       LDY #$03           - A:00 X:ff Y:0f SP:f7   -B  ZC
    * 0f7d  46 39       LSR $39            - A:00 X:ff Y:03 SP:f7   -B   C
    0f7f  2A          ROL A              - A:00 X:ff Y:03 SP:f7   -B
    0f80  88          DEY                - A:00 X:ff Y:03 SP:f7   -B  Z
    0f81  D0 FA       BNE $0F7D          - A:00 X:ff Y:02 SP:f7   -B

    """


    loc39 = acc

    y= 3
    acc = 0
    while y > 0: 
        cf = loc39 % 2
        loc39 = int(loc39 / 2)
        acc = acc + acc + cf
#        print "y = %d, loc39 =  %s acc   =  %s  cf=%d  " % (y,hex(loc39),hex(acc),cf)

        y = y - 1
        
        
    ret =  chars[acc]+chars[loc39]    
    return ret    
    
Debug=False

def nibval(str):
    nib=ord(str[0])
    val = 0
    if Debug:
        print "str0=%s" % str[0]
        print "nib=%d" % nib
        print hex(nib)
    if nib ==0x37:
        val = 0
    if nib > 0x31 and nib <= 0x36:
        val = 31-(0x36-nib)
    if nib >=0x41 and nib < 0x1B:
        val = nib-0x40
    if nib >=0x61 and nib < 0x7B:
        val = nib-0x60
        
    return val

    
    
# llll llll llll llll llll llll llll => 5 x 4 x 6  = 120 bits  => 15 bytes 


def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

    
def bytesfromint(val):
    ret = []
    tmp = val
    while tmp > 0:
        r = int(tmp % 256)
        ret = [r] + ret 
        tmp = int(tmp / 256)
    
    while len(ret)<15:
         ret = [0]+ ret 
        
    
    return ret
        
    
def mselinetobytes(str):
    ret = ""
    sum = 0
    for l in str:
        p = nibval(l)
        sum = sum * 32 + p
        if Debug:
            print p,"=",l,"=",sum
    
    ret = bytesfromint(sum) 
    if Debug:
        print "=",str,"=",sum,"=",ret,"="
    return ret
    

def msetxt2int(str):
    high=nibval(str[0])
    low=nibval(str[1])
    #print high,low
    return high * 32 + low, low*32+high

def sometests():
        if False:
            for l in 'ol'.split():
                print nibval(l)

            print asc2val("7")

            print asc2val("t")

                    
            print msetxt2int('77')    
            print msetxt2int('7a')    
            
            print msetxt2int('ey')    
            print msetxt2int('ew')    
            
            print repr(bitstring_to_bytes("010101010"))
            
            print mselinetobytes("llllllllllllllllllllllll")
            print mselinetobytes("aaaaaaaaaaaaaaaaaaaaaaaa")
            print mselinetobytes("777777777777777777777777")
            print mselinetobytes("a77777777777777777777777")
            print mselinetobytes("7a7777777777777777777777")
            print mselinetobytes("77a777777777777777777777")
            print mselinetobytes("777a77777777777777777777")
            print mselinetobytes("7777a7777777777777777777")
            
            print msetxt2int('c3')    
            print msetxt2int('7t')    
            print "ey",msetxt2int('ey')    
            print "eh",msetxt2int('eh')    
            print "a2",msetxt2int('a2')    
            print "eb",msetxt2int('eb')    
            print "aj",msetxt2int('aj')    
            #print msetxt2int('73')    
            
            print mse21(0x7000,bytes00)
            print mse21(0x704b,bytes4b)
            print mse21(0x7096,bytes96)



            #print chars8tobytes5("77777777")
            
            print mselinetobytes("773g36666666666666666666")
            print bytes00
            
            print "0x7000",mse21(0x7000,mselinetobytes("773g36666666666666666666"))
            print mse21(0x700f,mselinetobytes("666666666666666666666666"))
            print mse21(0x701e,mselinetobytes("666666666666666666666666"))
            print mse21(0x702d,mselinetobytes("666666666666666666666666"))
            print mse21(0x703c,mselinetobytes("66666iiii666666666666666"))
            print mse21(0x704b,mselinetobytes("777777777777777777777777"))
            print mse21(0x705a,mselinetobytes("777777777777777777777777"))
            print mse21(0x7069,mselinetobytes("777777777777777777777777"))
            print mse21(0x7078,mselinetobytes("777777777777777777777777"))
            print mse21(0x7087,mselinetobytes("777777777777777777777777"))
            print mse21(0x7096,mselinetobytes("666666666666666666666666"))

            """


            0fc6  A0 00       LDY #$00           - A:20 X:ff Y:0e SP:f5   -B   C
            0fc8  A5 14       LDA $14            - A:20 X:ff Y:00 SP:f5   -B  ZC
            0fca  85 3D       STA $3D            - A:4b X:ff Y:00 SP:f5   -B   C
            0fcc  B1 14       LDA ($14),Y        - A:4b X:ff Y:00 SP:f5   -B   C
            0fce  18          CLC                - A:00 X:ff Y:00 SP:f5   -B  ZC
            0fcf  65 3D       ADC $3D            - A:00 X:ff Y:00 SP:f5   -B  Z
            0fd1  0A          ASL A              - A:4b X:ff Y:00 SP:f5   -B
            0fd2  69 00       ADC #$00           - A:96 X:ff Y:00 SP:f5 N -B
            0fd4  85 3D       STA $3D            - A:96 X:ff Y:00 SP:f5 N -B
            0fd6  C8          INY                - A:96 X:ff Y:00 SP:f5 N -B
            0fd7  C0 0F       CPY #$0F           - A:96 X:ff Y:01 SP:f5   -B
            0fd9  D0 F1       BNE $0FCC          - A:96 X:ff Y:01 SP:f5 N -B"""
                
            #print loc39
            #print acc
            

            
            print "v.20"
            #print mse20(0x1c00,bytes00)
            print mse20(0x1c0f,mselinetobytes("666666666666666666666666"))
            print mse20(0x1c1e,mselinetobytes("777777777777777777777777"))



            print mse20(0x005a,mselinetobytes("rrssttuuvvwwxxyyzz666666"))
            print mse21(0x005a,mselinetobytes("rrssttuuvvwwxxyyzz666666"))
            

            print "0x003c",mse20(0x003c,mselinetobytes("7777 77g6 6666 6666 6666"))
            print "0xC03c",mse21(0xc03c,mselinetobytes("777777g6666666666666"))

            print "v 2.1"

            print "0xC000",mse21(0xc000,mselinetobytes("77777777777777777777")) # 77
            print "0xC00f",mse21(0xc00f,mselinetobytes("77777777777777777777")) # gp
            print "0xC01e",mse21(0xc01e,mselinetobytes("77777777777777777777")) # ga
            print "0xC02d",mse21(0xc02d,mselinetobytes("77777777777777777777")) # cr
            print mselinetobytes("777777g66666666666666666")
            print "20/0xC03c",mse20(0xc03c,mselinetobytes("777777g66666666666666666"))
            print "21/0xC03c",mse21(0xc03c,[0,0,0,0,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff])
            print "21/0xC04b",mse21(0xc04b,[0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff])

            print line24tobytes15("777777g6666666666666")
            # ges = ""
            # ges = ges + chars8tobytes5(str[0:8])
            # ges = ges + chars8tobytes5(str[8:16])
            # ges = ges + chars8tobytes5(str[16:24])
            # return ges
            get_bin = lambda x, n: format(x, 'b').zfill(n)
            thestr=""
            for v in "777777g66666666666666666":
                z = nibval(v)
                thestr = thestr + get_bin(z,5)
                print thestr
                bytes=[]
            
            while len(thestr) > 0:
                val = int(thestr[0:8],2)
                thestr= thestr [8:]
                print val, thestr
                bytes.append(val)

            print bytes
            #print bitstring_to_bytes(str).split()
            #print nibval("7")
    
if __name__=='__main__':
    
    
    print "21/0xC000/777777777777777777777777",mse21(0xc000,mselinetobytes("777777777777777777777777"))
    print "21/0xC00f/777777777777777777777777",mse21(0xc00f,mselinetobytes("777777777777777777777777"))
    print "21/0xC01e/777777777777777777777777",mse21(0xc01e,mselinetobytes("777777777777777777777777"))
    print "21/0xC02d/777777777777777777777777",mse21(0xc02d,mselinetobytes("777777777777777777777777"))
    print "21/0xC03c/777777g66666666666666666",mse21(0xc03c,mselinetobytes("777777g66666666666666666"))
    print "21/0xC04b/666666666666666666666666",mse21(0xc04b,mselinetobytes("666666666666666666666666"))
    