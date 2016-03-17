.pc = $4000 "Main Program"


lda $00

lda #$01
sta $d021

lda #$0d 
jsr $ffd2 

ldx #$3

loop2:
lda text,x
sta $0400,x
lda #$2
sta $d800,x
dex
bpl loop2



lda #$01
ldx $0400
lda #$01
ldx $d800
//#ldx #$00 

ldx #$c0
lda #$00
jsr $bdcd

lda #$0d 
jsr $ffd2 

ldx #$00
lda #$c0
jsr $bdcd


loop:
sta $d020
lda #$53
ldx #$54
ldy #$55
inc $d020
lda #$56

jmp loop

store:
	.byte 0
text:
	.byte 't','e','s','t'