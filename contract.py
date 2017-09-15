from typing import List
from parse import Parser, Instruction
import copy

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
            l += ', '.join(map(lambda arg: arg.value, self.assignTo)) + " = "
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
    def __init__(self, code):
        self.code = code
        self.blocks = Parser.parse(self.code)
        for block in self.blocks:
            for line in block.instructions:
                line.arguments = list(map(lambda arg: Output(arg), line.arguments or []))
        self.symbols = []
        self.line_blocks = []
        self._symbolIdx = 0

    def get_stack_args(self, num, block_copy: List[ContractLine], block_idx: int):
        block = self.line_blocks[block_idx]
        current_num = 0
        for line_num in range(len(block_copy) - 1, -1, -1):
            line = block_copy[line_num]
            if 'PUSH' in line.instruction.name:
                if current_num == num:
                    del block[line_num]
                    return line.args[0]
                current_num += 1
                continue
            if 'DUP' in line.instruction.name:
                print(line.args)
                if current_num == num:
                    del block[line_num]
                    return line.args[0]
                current_num += 1
                continue
            if 'SWAP' in line.instruction.name:
                v = 0
                while v < len(line.args):
                    if current_num == num:
                        if v == 0:
                            return line.args[-1]
                        elif v + 1 == len(line.args):
                            return line.args[0]
                        else:
                            return line.args[v]
                    v += 1
                    current_num += 1
                continue
            for var in line.assignTo[::-1]:
                if current_num == num:
                    var.use()
                    return var
                current_num += 1
        return Output('arg' + str(current_num - num))

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
                    block_copy = copy.copy(line)
                    while arg < operation.instruction.removed:
                        a = self.get_stack_args(arg, block_copy, block_idx)
                        in_variables.append(a)
                        arg += 1
                for i in range(operation.instruction.added):
                    out_variables.append(Output('var' + str(self._symbolIdx)))
                    self._symbolIdx += 1
                # if operation.
                line.append(ContractLine(address=operation.address, assignTo=out_variables, instruction=operation.instruction, args=in_variables))
                # self._symbolIdx += 1
                instr_idx += 1
            # for swap op codes, we have to wait until after parsing to remove them

            idx = 0
            while idx < len(line):
                if 'SWAP' in line[idx].instruction.name:
                    print('deleting ' + str(line[idx].instruction.name) )
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