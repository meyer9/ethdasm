import unittest

import contract


class TestContract(unittest.TestCase):
    def test_dup_swap(self):
        """
        Tests the following EVM code decompilation:
            PUSH 20
            PUSH 30
            DUP2
            SWAP2
            MUL
            ADD
        The output of this code should be 0x620 or 1568.
        """
        c = contract.Contract('6020603081910201')
        c.parse()
        self.assertIn(0x30, map(lambda l: l.value, c.line_blocks[0].lines[-2].args))
        self.assertIn(0x20, map(lambda l: l.value, c.line_blocks[0].lines[-2].args))
        self.assertIn(0x20, map(lambda l: l.value, c.line_blocks[0].lines[-1].args))
    def test_function_rollover(self):
        """
        Tests the following EVM code decompilation:
            PUSH 02
            PUSH 03
            JUMPDEST
            PUSH 02
            ADD
            JUMPDEST
            PUSH 04
            MUL
        There should be 2 different jump lines at the end of each block.
        """
        c = contract.Contract('600260035b6002015b600402')
        c.parse()
        self.assertIsInstance(c.line_blocks[0].lines[-1], contract.JumpLine)
        self.assertEqual(c.line_blocks[0].lines[-1].args[0].value, 2)
        self.assertTrue(c.line_blocks[0].lines[-1].args[0].is_variable)
        self.assertIsInstance(c.line_blocks[1].lines[-1], contract.JumpLine)
        self.assertEqual(c.line_blocks[1].lines[-1].args[0].value, 3)
        self.assertTrue(c.line_blocks[1].lines[-1].args[0].is_variable)

    def test_single_jumpdest(self):
        """
        Tests the following EVM code decompilation:
            JUMPDEST
        This should not crash.
        """
        c = contract.Contract('5b')
        c.parse()
    
    def test_math_simplification(self):
        """
        Tests basic math simplification:
            PUSH 02
            PUSH 02
            PUSH 03
            MUL
            MUL
        """
        c = contract.Contract('6002600260030202')
        c.parse()
        self.assertEqual(c.line_blocks[0].lines[0].args[0].value, 12)

if __name__ == '__main__':
    unittest.main()
