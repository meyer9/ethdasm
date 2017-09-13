"""
Stores all information about different opcodes.
"""
OPCODES = {
    '00': {
        'name': 'STOP',
        'removed': 0,
        'added': 0,
        'args': 0
    },
    '01': {
        'name': 'ADD',
        'removed': 2,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b: a + b
    },
    '02': {
        'name': 'MUL',
        'removed': 2,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b: a * b
    },
    '03': {
        'name': 'SUB',
        'removed': 2,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b: a - b
    },
    '04': {
        'name': 'DIV',
        'removed': 2,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b: a // b
    },
    '05': {
        'name': 'SDIV',
        'removed': 2,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b: a // b # FIXME
    },
    '06': {
        'name': 'MOD',
        'removed': 2,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b: a % b
    },
    '07': {
        'name': 'SMOD',
        'removed': 2,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b: a % b # FIXME
    },
    '08': {
        'name': 'ADDMOD',
        'removed': 3,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b, c: (a + b) % c 
    },
    '09': {
        'name': 'MULMOD',
        'removed': 3,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b, c: (a * b) % c

    },
    '0a': {
        'name': 'EXP',
        'removed': 2,
        'added': 1,
        'args': 0,
        'equivalent_function': lambda a, b: a ** b
    },
    '0b': {
        'name': 'SIGNEXTEND',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '10': {
        'name': 'LT',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '11': {
        'name': 'GT',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '12': {
        'name': 'SLT',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '13': {
        'name': 'SGT',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '14': {
        'name': 'EQ',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '15': {
        'name': 'ISZERO',
        'removed': 1,
        'added': 1,
        'args': 0
    },
    '16': {
        'name': 'AND',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '17': {
        'name': 'OR',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '18': {
        'name': 'XOR',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '19': {
        'name': 'NOT',
        'removed': 1,
        'added': 1,
        'args': 0
    },
    '1a': {
        'name': 'BYTE',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '20': {
        'name': 'SHA3',
        'removed': 2,
        'added': 1,
        'args': 0
    },
    '30': {
        'name': 'ADDRESS',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '31': {
        'name': 'BALANCE',
        'removed': 1,
        'added': 1,
        'args': 0
    },
    '32': {
        'name': 'ORIGIN',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '33': {
        'name': 'CALLER',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '34': {
        'name': 'CALLVALUE',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '35': {
        'name': 'CALLDATALOAD',
        'removed': 1,
        'added': 1,
        'args': 0
    },
    '36': {
        'name': 'CALLDATASIZE',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '37': {
        'name': 'CALLDATACOPY',
        'removed': 3,
        'added': 0,
        'args': 0
    },
    '38': {
        'name': 'CODESIZE',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '39': {
        'name': 'CODECOPY',
        'removed': 3,
        'added': 0,
        'args': 0
    },
    '3a': {
        'name': 'GASPRICE',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '3b': {
        'name': 'EXTCODESIZE',
        'removed': 1,
        'added': 1,
        'args': 0
    },
    '3c': {
        'name': 'EXTCODECOPY',
        'removed': 4,
        'added': 0,
        'args': 0
    },
    '40': {
        'name': 'BLOCKHASH',
        'removed': 1,
        'added': 1,
        'args': 0
    },
    '41': {
        'name': 'COINBASE',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '42': {
        'name': 'TIMESTAMP',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '43': {
        'name': 'NUMBER',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '44': {
        'name': 'DIFFICULTY',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '45': {
        'name': 'GASLIMIT',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '50': {
        'name': 'POP',
        'removed': 1,
        'added': 0,
        'args': 0
    },
    '51': {
        'name': 'MLOAD',
        'removed': 1,
        'added': 1,
        'args': 0
    },
    '52': {
        'name': 'MSTORE',
        'removed': 2,
        'added': 0,
        'args': 0
    },
    '53': {
        'name': 'MSTORE8',
        'removed': 2,
        'added': 0,
        'args': 0
    },
    '54': {
        'name': 'SLOAD',
        'removed': 1,
        'added': 1,
        'args': 0
    },
    '55': {
        'name': 'SSTORE',
        'removed': 2,
        'added': 0,
        'args': 0
    },
    '56': {
        'name': 'JUMP',
        'removed': 1,
        'added': 0,
        'args': 0
    },
    '57': {
        'name': 'JUMPI',
        'removed': 2,
        'added': 0,
        'args': 0
    },
    '58': {
        'name': 'PC',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '59': {
        'name': 'MSIZE',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '5a': {
        'name': 'GAS',
        'removed': 0,
        'added': 1,
        'args': 0
    },
    '5b': {
        'name': 'JUMPDEST',
        'removed': 0,
        'added': 0,
        'args': 0
    },
    'f0': {
        'name': 'CREATE',
        'removed': 3,
        'added': 1,
        'args': 0
    },
    'f1': {
        'name': 'CALL',
        'removed': 7,
        'added': 1,
        'args': 0
    },
    'f2': {
        'name': 'CALLCODE',
        'removed': 7,
        'added': 1,
        'args': 0
    },
    'f3': {
        'name': 'RETURN',
        'removed': 2,
        'added': 0,
        'args': 0
    },
    'f4': {
        'name': 'DELEGATECALL',
        'removed': 6,
        'added': 1,
        'args': 0
    },
    'ff': {
        'name': 'SUICIDE',
        'removed': 1,
        'added': 0,
        'args': 0
    }
}

for i in range(96, 128):
    OPCODES[hex(i)[2:]] = {
        'name': 'PUSH' + str(i - 95),
        'removed': 0,
        'added': 1,
        'args': i - 95
    }

for i in range(128, 144):
    OPCODES[hex(i)[2:]] = {
        'name': 'DUP' + str(i - 127),
        'removed': i - 127,
        'added': i - 126,
        'args': 0
    }

for i in range(144, 160):
    OPCODES[hex(i)[2:]] = {
        'name': 'SWAP' + str(i - 143),
        'removed': i - 142,
        'added': i - 142,
        'args': 0
    }

for i in range(160, 165):
    OPCODES[hex(i)[2:]] = {
        'name': 'LOG' + str(i - 160),
        'removed': i - 158,
        'added': 0,
        'args': 0
    }

for i in range(0, 256):
    if not OPCODES.get(hex(i)[2:]):
        OPCODES[hex(i)[2:]] = {
            'name': 'THROW',
            'removed': 0,
            'added': 0,
            'args': 0
        }
