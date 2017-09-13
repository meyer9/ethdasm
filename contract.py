from typing import List
from parse import Parser, Instruction

class ContractLine():
    """
    Represents one line of code in the contract according to our pseudo-code.abs
    In this case, args contains symbols.
    """
    address: int
    assignTo: List[str]
    instruction: Instruction
    def __init__(self, address: int, assignTo: List[str], instruction: Instruction, args):
        self.address = address
        self.assignTo = assignTo
        self.instruction = instruction
        self.args = args

    def __str__(self):
        l = ""
        if self.assignTo:
            l += ', '.join(self.assignTo) + " = "
        if not self.instruction.infix_operator:
            l += self.instruction.name + '({0})'.format(', '.join(self.args or []))
        else:
            l += '{0} {1} {2}'.format(self.args[0], self.instruction.infix_operator, self.args[1])
        return l

    def __repr__(self):
        return repr(self.instruction)

class Contract():
    def __init__(self, code):
        self.code = code
        self.blocks = Parser.parse(self.code)
        self.symbols = []
        self.line_blocks = []
        self._symbolIdx = 0

    def get_stack_args(self, num, block: List[ContractLine]):
        block = self.line_blocks[block]
        current_num = 0
        for line_num in range(len(block) - 2, -1, -1):
            line = block[line_num]
            if 'PUSH' in line.instruction.name:
                if current_num == num:
                    del block[line_num]
                    return 1, line.args[0]
                current_num += 1
            if 'DUP' in line.instruction.name:
                if current_num == num:
                    del block[line_num]
                    return 0, line.args[-1]
                current_num += 1
            for var in line.assignTo[::-1]:
                if current_num == num:
                    return 0, var
                current_num += 1
        return 0, 'arg' + str(num - current_num)

    def parse(self) -> List[ContractLine]:
        self.line_blocks = []
        block_idx = 0
        for block in self.blocks:
            line = []
            self.line_blocks.append(line)
            instr_idx = 0
            for operation in block.instructions:
                in_variables = []
                out_variables = []
                if operation.arguments:
                    in_variables = operation.arguments
                else:
                    arg = 0
                    while arg < operation.instruction.removed:
                        new_instr_idx, a = self.get_stack_args(arg, block_idx)
                        in_variables.append(a)
                        instr_idx += new_instr_idx
                        arg += 1
                for i in range(operation.instruction.added):
                    out_variables.append('var' + str(self._symbolIdx))
                    self._symbolIdx += 1
                # if operation.
                line.append(ContractLine(address=operation.address, assignTo=out_variables, instruction=operation.instruction, args=in_variables))
                # self._symbolIdx += 1
                instr_idx += 1
            block_idx += 1
        return self.line_blocks

def main():
    with open('contract.evm', 'r') as contract:
        contract = Contract(contract.read())
        blocks = contract.parse()
        for lines in blocks:
            print('===============BLOCK==============')
            for line in lines:
                print('[{0}] {1}'.format(hex(line.address), str(line)))

if __name__ == '__main__':
    main()