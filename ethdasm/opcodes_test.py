import unittest

from ethdasm.opcodes import get_opcode_by_code, get_opcode_by_mnemonic


class TestOpcodes(unittest.TestCase):
    def test_get_opcode_by_mnemonic(self):
        """
        Attempts to retrieve the PUSH1 opcode.
        """
        self.assertEqual(get_opcode_by_mnemonic('PUSH1').name, 'PUSH1')
    def test_get_opcode_by_code(self):
        """
        Tests getting the opcode with code 02 (MUL)
        """
        self.assertEqual(get_opcode_by_code('02').name, 'MUL')

if __name__ == '__main__':
    unittest.main()
