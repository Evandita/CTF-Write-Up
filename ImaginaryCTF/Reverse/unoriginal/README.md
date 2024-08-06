# Problem

## Description
i like elf reversing

## Attachments
https://cybersharing.net/s/8330af8ef6c673a8

# Solution

To reverse engineer the executable file, I use radare2 in linux with Ghidra Decompiler extension. Using the `aa` and `afl` command in radare2, I find a list of functions in the file.

```
0x00001090    1     11 sym.imp.puts
0x000010a0    1     11 sym.imp.__stack_chk_fail
0x000010b0    1     11 sym.imp.printf
0x000010c0    1     11 sym.imp.strcmp
0x000010d0    1     11 sym.imp.gets
0x000010e0    1     37 entry0
0x00001110    4     34 sym.deregister_tm_clones
0x00001140    4     51 sym.register_tm_clones
0x00001180    5     54 sym.__do_global_dtors_aux
0x00001080    1     11 fcn.00001080
0x000011c0    1      9 sym.frame_dummy
0x00001290    1     13 sym._fini
0x000011c9    9    197 main
0x00001000    3     27 sym._init
```

A main function is available here, so we can take a look at it using the Ghidra Decompiler command `pdg` in radare2

```c
ulong main(void)

{
    int32_t iVar1;
    uchar *puVar2;
    uchar *puVar3;
    int64_t in_FS_OFFSET;
    ulong uStack_60;
    uchar auStack_58 [12];
    int32_t iStack_4c;
    uint8_t auStack_48 [56];
    int64_t iStack_10;
    
    iStack_10 = *(in_FS_OFFSET + 0x28);
    *(*0x20 + -0x60) = 0x11f8;
    sym.imp.printf("Enter your flag here: ");
    puVar2 = *0x20 + -0x58;
    *(*0x20 + -0x58 + -8) = 0x1209;
    sym.imp.gets(&stack0xffffffffffffffb8);
    for (iStack_4c = 0; iStack_4c == 0x2f || SBORROW4(iStack_4c, 0x2f) != iStack_4c + -0x2f < 0;
        iStack_4c = iStack_4c + 1) {
        (&stack0xffffffffffffffb8)[iStack_4c] = (&stack0xffffffffffffffb8)[iStack_4c] ^ 5;
    }
    *(puVar2 + -8) = 0x124a;
    iVar1 = sym.imp.strcmp(&stack0xffffffffffffffb8, "lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx");
    if (iVar1 == 0) {
        *(puVar2 + -8) = 0x125d;
        sym.imp.puts("Correct!");
        puVar3 = puVar2 + 0;
    }
    else {
        *(puVar2 + -8) = 0x1273;
        sym.imp.puts("Incorrect.");
        puVar3 = puVar2;
    }
    if (iStack_10 != *(in_FS_OFFSET + 0x28)) {
    // WARNING: Subroutine does not return
        *(puVar3 + -8) = 0x128c;
        sym.imp.__stack_chk_fail();
    }
    return 0;
}
```

Well this line certainly looks interesting...

```c
    iVar1 = sym.imp.strcmp(&stack0xffffffffffffffb8, "lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx");
```

So it looks like the resulted string looks scrambled, so lets take a look what kind of operation happen before this line.

```c
    sym.imp.gets(&stack0xffffffffffffffb8);
    for (iStack_4c = 0; iStack_4c == 0x2f || SBORROW4(iStack_4c, 0x2f) != iStack_4c + -0x2f < 0;
        iStack_4c = iStack_4c + 1) {
        (&stack0xffffffffffffffb8)[iStack_4c] = (&stack0xffffffffffffffb8)[iStack_4c] ^ 5;
    }
```

It seems that the program takes a string input from the user, then does a **XOR** operation with the value **5** for every character. Since the for loop happens from iteration value 0 to 0x2f, we can also get that the string must be 32 characters long.

Now, it is clear that the string input must matched ```"lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx"``` after the **XOR** operation. Note that the **XOR** operation is reversible, so to get the right string input we can **XOR** the result string with the value 5.

This python program below should do the job

```python
result = "lfqc~opvqZdkjqm`wZcidbZfm`fn`wZd6130a0`0``761gdx"
input = ""

for char in result:
    input += chr(ord(char) ^ 5)

print(input)
```

This will give the flag

**ictf{just_another_flag_checker_a3465d5e5ee234ba}**