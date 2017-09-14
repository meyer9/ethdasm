# ethdasm
ethdasm aims to be a disassembler tool for the EVM. It will feature symbol detection, math simplification, and control flow graph generation.

## Prerequisites
- Python 3.5 or greater

## Example Output
```
; Procedure 0x4
[     0x4] | MSTORE               | ['40', '60']
[     0x5] | CALLDATASIZE         | None
[     0x6] | ISZERO               | None
[     0xa] | JUMPI                | ['002a']
[     0xf] | PUSH29               | ['100000000000000000000000000000000000000000000000000000000']
[    0x12] | CALLDATALOAD         | ['00']
[    0x13] | DIV                  | None
[    0x14] | PUSH4                | ['41c0e1b5']
[    0x19] | DUP2                 | None
[    0x1a] | EQ                   | None
[    0x1e] | JUMPI                | ['0070']
[    0x1f] | DUP1                 | None
[    0x20] | PUSH4                | ['f3fef3a3']
[    0x25] | EQ                   | None
[    0x29] | JUMPI                | ['009f']
```

## Symbol identifier
One thing that makes ethdasm very powerful is it's ability to identify symbols in the code. For example, a smart contract header looks something like this without symbol identification:
```
PUSH1 0x60
PUSH1 0x40
MSTORE
CALLDATASIZE
ISZERO
PUSH2 0x002a
JUMPI
PUSH1 0xe0
PUSH1 0x02
EXP
PUSH1 0x00
CALLDATALOAD
DIV
PUSH4 0x41c0e1b5
DUP2
EQ
PUSH2 0x0070
JUMPI
DUP1
PUSH4 0xf3fef3a3
EQ
PUSH2 0x009f
JUMPI
```

First, we resolve all of the math and static code that produces the same output every time:
```
[     0x4] | MSTORE               | ['40', '60']
[     0x5] | CALLDATASIZE         | None
[     0x6] | ISZERO               | None
[     0x7] | PUSH2                | ['002a']
[     0xa] | JUMPI                | None
[     0xf] | PUSH29               | ['100000000000000000000000000000000000000000000000000000000']
[    0x12] | CALLDATALOAD         | ['00']
[    0x13] | DIV                  | None
[    0x14] | PUSH4                | ['41c0e1b5']
[    0x19] | DUP2                 | None
[    0x1a] | EQ                   | None
[    0x1b] | PUSH2                | ['0070']
[    0x1e] | JUMPI                | None
[    0x1f] | DUP1                 | None
[    0x20] | PUSH4                | ['f3fef3a3']
[    0x25] | EQ                   | None
[    0x26] | PUSH2                | ['009f']
[    0x29] | JUMPI                | None
```

Then, we resolve symbols within that code to make it much more human readable:
```
[0x4] MSTORE(40, 60)
[0x5] var0 = CALLDATASIZE()
[0x6] var1 = ISZERO(var0)
[0xa] JUMPI(002a, var1)
[0x12] var4 = CALLDATALOAD(00)
[0x13] var5 = var4 // 100000000000000000000000000000000000000000000000000000000
[0x1a] var10 = 41c0e1b5 == var5
[0x1e] JUMPI(0070, var10)
[0x25] var15 = f3fef3a3 == var10
[0x29] JUMPI(009f, var15)
```