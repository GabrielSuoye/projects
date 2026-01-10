section .data
    msg db "Hello, World!", 0xA   ; The string and a newline character (0xA)
    len equ $ - msg             ; Length of the message 

section .text
    global _start               ; Declares the entry point for the linker

_start:
    ; System call for sys_write
    mov eax, 4                  ; Syscall number for 'Write' (4) goes into EAX
    mov ebx, 1                  ; File descriptor 1 (stdout) goes into EBX
    mov ecx, msg                ; Address of the string to write goes into ECX
    mov edx, len                ; Length of the string goes into EDX
    int 0x80                    ; Trigger the kernel interupt to execute the syscall

    ; System call for sys_exit
    mov eax, 1                  ; Syscall number for 'Exit' (1) goes into EAX
    xor ebx, ebx                ; Exit code 0 (success) goes into EBX (clears EBX)
    int 0x80                    ; Trigger the kernel interupt to execute the syscall
