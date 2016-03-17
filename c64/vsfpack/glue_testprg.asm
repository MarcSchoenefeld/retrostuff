.pc = $0400 "Main Program"
sei
lda #$37
lda #$91 
ldy #$55
ldx #$54
cli 
jmp $400e 
