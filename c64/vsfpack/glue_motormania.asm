.pc = $c000 "Main Program"
sei


ldx #$40
loop:
lda vicregs,x
sta $d000,x
dex 
bpl loop

lda #$3f
sta $dd00

lda #$fd
sta $01
lda #$10 
ldy #$18
ldx #$0

cli 
jmp $e23a 

vicregs:
	
 .byte $4e,$ad,$7e,$ad,$0,$cd,$ae,$ad,$17,$36,$17,$36,$17,$36,$0,$0
 .byte $70,$1b,$65,$0,$0,$7b,$f8,$7b,$1c,$0,$1,$0,$c0,$7b,$70,$71
 .byte $e,$f,$1,$0,$3,$4,$1,$7,$7,$8,$7,$7,$a,$2,$c,$0
 .byte $0,$0,$0,$0,$0,$0,$76,$0,$0,$0,$0,$0,$0,$0,$0,$00
