1: .section __TEXT,__text
2: .globl _main
3: _main:
4:     movq $0, %rax;            # move 0 to rax
5:     movq $4, %rbx;            # move 4 to rbx
6: loop:
7:     addq $5, %rax;            # add 5 to rax (rax += 5)
8:     subq $1, %rbx;            # subtract 1 to rbx (rbx -= 1)
9:     cmpq $0, %rbx;            # compare 0 and rbx
10:     jne  loop                 # if Not Equal, jump to 'loop'
11:
12:     movq %rax, %rdi           # set result to the exit code
13:     movq $0x2000001, %rax     # system call $1 with $0x2000000 offset
14:     syscall
