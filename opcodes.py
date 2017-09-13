"""
Stores all information about different _OPCODES.
"""
import collections
import typing

class OpCode(typing.NamedTuple):
    name: str
    removed: int
    added: int
    args: int
    equivalent_function: typing.Callable
    infix_operator: str

_OPCODES = {
  '00': OpCode(name = 'STOP', removed = 0, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '01': OpCode(name = 'ADD', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a + b, infix_operator='+'),
  '02': OpCode(name = 'MUL', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a * b, infix_operator='*'),
  '03': OpCode(name = 'SUB', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a - b, infix_operator='-'),
  '04': OpCode(name = 'DIV', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a // b, infix_operator='//'),
  '05': OpCode(name = 'SDIV', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a // b, infix_operator='//'), #
  '06': OpCode(name = 'MOD', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a % b, infix_operator='%'),
  '07': OpCode(name = 'SMOD', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a % b, infix_operator='%'),
  '08': OpCode(name = 'ADDMOD', removed = 3, added = 1, args = 0, equivalent_function = lambda a, b, c: (a + b) % c, infix_operator=None),
  '09': OpCode(name = 'MULMOD', removed = 3, added = 1, args = 0, equivalent_function = lambda a, b, c: (a * b) % c, infix_operator=None),
  '0a': OpCode(name = 'EXP', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a ** b, infix_operator='**'),
  '0b': OpCode(name = 'SIGNEXTEND', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '10': OpCode(name = 'LT', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='<'),
  '11': OpCode(name = 'GT', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='>'),
  '12': OpCode(name = 'SLT', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='<'),
  '13': OpCode(name = 'SGT', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='>'),
  '14': OpCode(name = 'EQ', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator='=='),
  '15': OpCode(name = 'ISZERO', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '16': OpCode(name = 'AND', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a & b, infix_operator='&'),
  '17': OpCode(name = 'OR', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a | b, infix_operator='|'),
  '18': OpCode(name = 'XOR', removed = 2, added = 1, args = 0, equivalent_function = lambda a, b: a ^ b, infix_operator='^'),
  '19': OpCode(name = 'NOT', removed = 1, added = 1, args = 0, equivalent_function = lambda a: ~a, infix_operator=None),
  '1a': OpCode(name = 'BYTE', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '20': OpCode(name = 'SHA3', removed = 2, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '30': OpCode(name = 'ADDRESS', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '31': OpCode(name = 'BALANCE', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '32': OpCode(name = 'ORIGIN', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '33': OpCode(name = 'CALLER', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '34': OpCode(name = 'CALLVALUE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '35': OpCode(name = 'CALLDATALOAD', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '36': OpCode(name = 'CALLDATASIZE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '37': OpCode(name = 'CALLDATACOPY', removed = 3, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '38': OpCode(name = 'CODESIZE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '39': OpCode(name = 'CODECOPY', removed = 3, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '3a': OpCode(name = 'GASPRICE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '3b': OpCode(name = 'EXTCODESIZE', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '3c': OpCode(name = 'EXTCODECOPY', removed = 4, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '40': OpCode(name = 'BLOCKHASH', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '41': OpCode(name = 'COINBASE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '42': OpCode(name = 'TIMESTAMP', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '43': OpCode(name = 'NUMBER', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '44': OpCode(name = 'DIFFICULTY', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '45': OpCode(name = 'GASLIMIT', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '50': OpCode(name = 'POP', removed = 1, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '51': OpCode(name = 'MLOAD', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '52': OpCode(name = 'MSTORE', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '53': OpCode(name = 'MSTORE8', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '54': OpCode(name = 'SLOAD', removed = 1, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '55': OpCode(name = 'SSTORE', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '56': OpCode(name = 'JUMP', removed = 1, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '57': OpCode(name = 'JUMPI', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  '58': OpCode(name = 'PC', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '59': OpCode(name = 'MSIZE', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '5a': OpCode(name = 'GAS', removed = 0, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  '5b': OpCode(name = 'JUMPDEST', removed = 0, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  'f0': OpCode(name = 'CREATE', removed = 3, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  'f1': OpCode(name = 'CALL', removed = 7, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  'f2': OpCode(name = 'CALLCODE', removed = 7, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  'f3': OpCode(name = 'RETURN', removed = 2, added = 0, args = 0, equivalent_function = None, infix_operator=None),
  'f4': OpCode(name = 'DELEGATECALL', removed = 6, added = 1, args = 0, equivalent_function = None, infix_operator=None),
  'ff': OpCode(name = 'SUICIDE', removed = 1, added = 0, args = 0, equivalent_function = None, infix_operator=None)
}

for i in range(96, 128):
    _OPCODES[hex(i)[2:]] = OpCode(name='PUSH' + str(i - 95), removed=0, added=1, args=i-95, equivalent_function=None, infix_operator=None)

for i in range(128, 144):
    _OPCODES[hex(i)[2:]] = OpCode(name='DUP' + str(i - 127), removed=i-127, added=i-126, args=0, equivalent_function=None, infix_operator=None)

for i in range(144, 160):
    _OPCODES[hex(i)[2:]] = OpCode(name='SWAP' + str(i - 143), removed=i-142, added=i-142, args=0, equivalent_function=None, infix_operator=None)

for i in range(160, 165):
    _OPCODES[hex(i)[2:]] = OpCode(name='LOG' + str(i - 160), removed=i-158, added=0, args=0, equivalent_function=None, infix_operator=None)

for i in range(0, 256):
    if not _OPCODES.get(hex(i)[2:].zfill(2)):
        _OPCODES[hex(i)[2:]] = OpCode('THROW', 0, 0, 0, None, None)

def get_opcode_by_code(sym):
    return _OPCODES[sym]

def get_opcode_by_mnemonic(mne):
    i = 0
    while _OPCODES[hex(i)[2:].zfill(2)].name != mne:
        i += 1
    return _OPCODES[hex(i)[2:].zfill(2)]