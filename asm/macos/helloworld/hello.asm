global _main

section .data

str_hello:   db  "Hello World", 0x0a

section .text

_main:
    mov rax, 0x2000004

    mov rdi, 1

    mov rsi, str_hello

    mov rdx, 13

    syscall

    mov rax, 0x2000001

    mov rdi, 0

    syscall
