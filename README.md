# ethdasm
[![Build Status](https://travis-ci.org/meyer9/ethdasm.svg?branch=master)](https://travis-ci.org/meyer9/ethdasm)
[![Coverage Status](https://coveralls.io/repos/github/meyer9/ethdasm/badge.svg?branch=master)](https://coveralls.io/github/meyer9/ethdasm?branch=master)

ethdasm aims to be a disassembler tool for the EVM. It will feature symbol detection and math simplification. I wrote this for fun and it possibly has some bugs. If you think this is neat, send some ether. If you develop a feature, send a PR. If you find a bug, submit an issue. If you want to talk, my email is my first name, my last name, plus 2000@gmail.com.

ETH: 0x56489eCd3A53bF6407438c28112Ae6956BB5b1EA

Thank you so much for the donations!

## Prerequisites
- Python 3.5 or greater

## Usage
```
usage: ethdasm.py [-h] [--decompile] [--disassemble] [--out OUT] input

positional arguments:
  input          input hex file to parse

optional arguments:
  -h, --help     show this help message and exit
  --decompile    decompiles the contract into a python-like pseudo-code
  --disassemble  disassembly contract into simplified op-codes
  --out OUT      outputs to a file; outputs to STDOUT if not specified
```

## Symbol identifier
One thing that makes ethdasm very powerful is it's ability to identify symbols in the code. For example, a smart contract header looks something like this:
```
; Procedure 0x4
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

We can also resolve this into a python-like pseudo-code.
```python
def main():
	MSTORE(40, 60)
	var1 = CALLDATASIZE()
	var2 = ISZERO(var1)
	if var2: func1()
	var3 = CALLDATALOAD(00)
	var4 = var3 // 100000000000000000000000000000000000000000000000000000000
	var5 = var4 == 41c0e1b5
	if var5: func2()
	var6 = f3fef3a3 == var4
	if var6: func3()
```

There is also a complete contract source, bytecode, disassembled bytecode and decompiled bytecode example in the example directory of the repository.
