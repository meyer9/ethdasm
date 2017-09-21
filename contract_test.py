import unittest

import contract


class TestStringMethods(unittest.TestCase):
    def test_dup_swap(self):
        """
        Tests the following EVM code decompilation:
            PUSH 20
            PUSH 30
            DUP2
            SWAP2
            MUL
            ADD
        The output of this code should be 620.
        """
        c = contract.Contract('6020603081910201')
        c.parse()
        self.assertEqual(c.line_blocks[0][-2].args[0].value, 'var0')
        self.assertEqual(c.line_blocks[0][-2].args[1].value, 'var1')
        self.assertEqual(c.line_blocks[0][-1].args[1].value, 'var0')


if __name__ == '__main__':
    unittest.main()
