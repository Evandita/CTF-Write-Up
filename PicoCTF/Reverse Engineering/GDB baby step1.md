# Problem

Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.

Disassemble [this](https://artifacts.picoctf.net/c/512/debugger0_a).

# Solutions

The problem is pretty simple, it wants us to debug an executable file and find the value of a register in a certain point. I am going to show the solution for 2 different debugger, which is GDB debugger and Radare2.

## Solution 1 (GDB)

1. Download the file, then make it runnable. In this example, my file name is `debugger0_a`

```bash
chmod +x debugger0_a
```

2. Make sure first to have GDB installed in your Linux machine, then start the GDB debugger

```bash
gdb ./debugger0_a
```

3. Make a breakpoint in the main function

```bash
b main
```

4. Now start debugging

```bash
run
```

5. After halted in the main function, keep stepping in until you reach the end of the main function. In assembly debugging, you can use `stepi` or `next` to step.

6. Check the value of register `eax` or `rax` in the debugger. It should be 0x86342.

7. Convert that value in decimal using a calculator and you should get 549.698.

8. From the value, you can create the flag **picoCTF{549698}**

## Solution 2 (Radare2)

1. Download the file, then make it runnable. In this example, my file name is `debugger0_a`

```bash
chmod +x debugger0_a
```

2. Make sure first to have Radare2 installed in your Linux machine, then start Radare2 on the downloaded file in debugging mode

```bash
r2 -d debugger0_a
```

3. Analyze the binary file to check for functions

```bash
aa
```

4. List all the function availale

```bash
afl
```

It should show something like this

```bash
0x55ac5a8d5040    1     46 entry0
0x55ac5a8d7fe0    1   4129 reloc.__libc_start_main
0x55ac5a8d5070    4     34 sym.deregister_tm_clones
0x55ac5a8d50a0    4     51 sym.register_tm_clones
0x55ac5a8d50e0    5     54 sym.__do_global_dtors_aux
0x55ac5a8d5030    1     11 fcn.55ac5a8d5030
0x55ac5a8d5120    1      9 sym.frame_dummy
0x55ac5a8d5000    3     27 sym._init
0x55ac5a8d51b0    1      5 sym.__libc_csu_fini
0x55ac5a8d51b8    1     13 sym._fini
0x55ac5a8d5140    4    101 sym.__libc_csu_init
0x55ac5a8d5129    1     22 main
```

From here, we know that the address of the main function is `0x55ac5a8d5129`.

5. Go to the main function

```bash
s 0x55ac5a8d5129
```

or

```bash
s main
```

6. Enter visual mode

```bash
V
```

Choose the layout that suites you by pressing `p`

7. Set the cursor to the end of main function. You can set the cursor by using the  `up arrow` and `down arrow` in the keyboard.

8. Once set, press `f2` to set a breakpoint, then press `f9` to run. and you should get the value of register `eax` or `rax` the same, which is 0x86342. If you missed the breakpoint, you can press `f7` or `f8` to step in.

9. Convert that value in decimal using a calculator and you should get 549.698.

10. From the value, you can create the flag **picoCTF{549698}**

