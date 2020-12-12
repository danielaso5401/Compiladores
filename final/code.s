.data
out_string0: .asciiz"5.0"
.text
main:
li $v0, 4 
la $a0, out_string0
syscall 
li $t1, 5
jr $ra
