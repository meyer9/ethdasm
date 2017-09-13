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