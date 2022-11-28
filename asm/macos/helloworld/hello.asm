section .data
	msg db 'Hello, world!', 0x0a
	len equ $ - msg

section .text
	global _main		; '_main'を外部参照可能に
_main:
	; SYSCALL: write(1, msg, len);
	mov rax, 0x2000004	; MacOSにおけるwrite関数の番号
	mov rdi, 1		; write()の第1引数。標準出力へ
	mov rsi, msg		; write()第2引数
	mov rdx, len		; write()第3引数
	syscall

	; SYSCALL: exit(0)
	mov rax, 0x2000001	; exit関数の番号
	mov rdi, 0		; 正常終了
	syscall
