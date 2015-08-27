section .data
segment .bss
sum resb 1

section .text
global _start

_start:
mov eax, rax, '1'
sub eax, rax, '0'
mov ebx, rbx, '2'
sub ebx, rbx, '0'
add eax, rax, rbx
add eax, rax, '0'
mov [sum], rax
mov ecx, rcx, sum
mov edx, rdx, 1
mov ebx, rbx, 1
mov eax, rax, 4
int 0x80
mov eax, rax, 1
int 0x80
