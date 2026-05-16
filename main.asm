section .data 
        msg db "Enter multiple numbers that you want to add (max = 10)", 0xA
        len equ $ - msg
        msg2 db "Sum = ", 0xA
        len equ $ - msg

section .bss
        nums resd 10 

section .text
        global _start

_start:
    ; syscall write
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, len
    int 0x80

    ; syscall read
    mov eax, 3
    mov ebx, 2
    mov ecx, nums
    mov edx, 10
    int 0x80

    ; syscall add








    ; exit syscall
    mov eax, 1
    int 0x80
