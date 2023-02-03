section .data
str:        db           "hello, world",0x0A
len:        equ          $ - str

    WRITE   equ     0x2000004
    EXIT    equ     0x2000001

section .text
global _main

_main:
    mov     rax,    WRITE
    mov     rdi,    1
    mov     rsi,    str
    mov     rdx,    len
    syscall

    mov     rax,    EXIT
    xor     rdi,    rdi
    syscall
