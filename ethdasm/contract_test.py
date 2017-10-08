import unittest

from ethdasm.contract import Contract, JumpLine


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
        c = Contract('6020603081910201')
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
        c = Contract('600260035b6002015b600402')
        c.parse()
        self.assertIsInstance(c.line_blocks[0].lines[-1], JumpLine)
        self.assertEqual(c.line_blocks[0].lines[-1].args[0].value, 2)
        self.assertTrue(c.line_blocks[0].lines[-1].args[0].is_variable)
        self.assertIsInstance(c.line_blocks[1].lines[-1], JumpLine)
        self.assertEqual(c.line_blocks[1].lines[-1].args[0].value, 3)
        self.assertTrue(c.line_blocks[1].lines[-1].args[0].is_variable)

    def test_single_jumpdest(self):
        """
        Tests the following EVM code decompilation:
            JUMPDEST
        This should not crash.
        """
        c = Contract('5b')
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
        c = Contract('6002600260030202')
        c.parse()
        self.assertEqual(c.line_blocks[0].lines[0].args[0].value, 12)
    
    def test_jump_arg_optimization(self):
        """
        Tests jump arg optimization:
            PUSH 03
            JUMP
            JUMPDEST
            PUSH 02
            PUSH 03
            MLOAD
            PUSH 0c
            JUMPI
            JUMPDEST
            THROW
        The conditional jump should reference func2.
        """
        c = Contract('6003565b6002600351600c575bfe')
        c.parse()
        self.assertEqual(c.line_blocks[1].lines[-2].jump_to, 'func2')
    
    def test_push_error(self):
        """
        Tests push error where an instruction tries to push to the stack at the end of a contract.abs
            PUSH ?
        This should not crash.
        """
        c = Contract('64')
        c.parse()

    def test_push_0(self):
        c = Contract('6000600201')
        c.parse()
    
    def test_neg_numbers(self):
        c = Contract('6023602003')
        c.parse()

if __name__ == '__main__':
    unittest.main()
