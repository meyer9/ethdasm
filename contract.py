from typing import List

from opcodes import OpCode
from parse import Parser, Instruction, Block


class ContractLine():
    """
    Represents one line of code in the contract according to our pseudo-code.abs
    In this case, args contains symbols.
    """
    address: int
    assign_to: List[str]
    instruction: Instruction
    args: List

    def __init__(self, address: int, assign_to: List[str], instruction: OpCode, args: List):
        self.address = address
        self.assign_to = assign_to
        self.instruction = instruction
        self.args = args

    def __str__(self):
        l = ""
        if self.assign_to:
            l += ', '.join(map(lambda arg: arg.value, self.assign_to)) + " = "
        if not self.instruction.infix_operator:
            l += self.instruction.name + '({0})'.format(', '.join(map(str, self.args) or []))
        else:
            l += '{0} {1} {2}'.format(self.args[0], self.instruction.infix_operator, self.args[1])
        return l

    def __repr__(self):
        return repr(self.instruction)

class Output():
    def __init__(self, value):
        self.value = value
        self.used = False
    def use(self):
        self.used = True
    def __str__(self):
        return self.value

class Contract():
    line_blocks: List[List[ContractLine]]
    blocks: List[Block]

    def __init__(self, code):
        self.code = code
        self.blocks = Parser.parse(self.code)
        for block in self.blocks:
            for line in block.instructions:
                line.arguments = list(map(lambda arg: Output(arg), line.arguments or []))
        self.symbols = []
        self.line_blocks = []
        self._symbolIdx = 0

    def get_stack_args(self, block_idx: int) -> Output:
        block = self.line_blocks[block_idx]
        for line_num in range(len(block) - 1, -1, -1):
            line = block[line_num]
            if 'DUP' in line.instruction.name:
                i = 0
                while i < len(line.assign_to):
                    if not line.assign_to[i].used:
                        line.assign_to[i].use()
                        if i == 0:
                            return line.args[-1]
                        else:
                            return line.args[i - 1]
                    i += 1
            if 'SWAP' in line.instruction.name:
                i = 0
                while i < len(line.assign_to):
                    if not line.assign_to[i].used:
                        line.assign_to[i].use()
                        if i == 0:
                            return line.args[-1]
                        elif i == len(line.assign_to) - 1:
                            return line.args[0]
                        else:
                            return line.args[i]
                    i += 1
            for var in line.assign_to[::-1]:
                if not var.used:
                    var.use()
                    return var
        return Output('arg')

    def parse(self) -> List[List[ContractLine]]:
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
                        a = self.get_stack_args(block_idx)
                        in_variables.append(a)
                        arg += 1
                for i in range(operation.instruction.added):
                    out_variables.append(Output('var' + str(self._symbolIdx)))
                    self._symbolIdx += 1
                # if operation.
                instruction = ContractLine(address=operation.address, assign_to=out_variables,
                                           instruction=operation.instruction, args=in_variables)
                line.append(instruction)
                # self._symbolIdx += 1
                instr_idx += 1
            # for swap op codes, we have to wait until after parsing to remove them

            idx = 0
            while idx < len(line):
                if 'SWAP' in line[idx].instruction.name or 'DUP' in line[idx].instruction.name:
                    del line[idx]
                    idx -= 1
                idx += 1
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