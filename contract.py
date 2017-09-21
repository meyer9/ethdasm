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
    """
    Represents the output of an instruction. Also can be considered
    a single value on the stack. Can be used.
    """
    def __init__(self, value):
        self.value = value
        self.used = False
    def use(self):
        """
        Use the value on the stack. Once used, this value should not be
        used again.
        """
        self.used = True
    def __str__(self):
        return self.value


class ContractBlock:
    
    args_needed: int
    lines: List[ContractLine]
    name: str
    indentation_level: int

    def __init__(self, name):
        self.args_needed = 0
        self.lines = []
        self.name = name
        self.indentation_level = 1
    
    def add_line(self, line: ContractLine):
        self.lines.append(line)
    
    def __str__(self):
        return "def {}({}):".format(self.name, ", ".join(map(lambda x: "arg" + str(x), range(self.args_needed))))


class Contract():
    """
    Represents an entire Ethereum contract. Keeps track of symbols,
    parses opcodes into pseudo-code, and simplifies the pseudo-code.
    """
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
        self.functions = {}

    def get_stack_args(self, block_idx: int) -> Output:
        block = self.line_blocks[block_idx].lines
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
        return None

    def parse(self) -> List[List[ContractLine]]:
        self.line_blocks = []
        block_idx = 0
        func_num = 0
        for block in self.blocks:
            line = ContractBlock("func" + str(func_num))
            func_num += 1
            self.functions[block.instructions[0].address] = line
            self.line_blocks.append(line)
            instr_idx = 0
            for operation in block.instructions:
                in_variables = []
                out_variables = []
                if operation.arguments:
                    in_variables = operation.arguments
                else:
                    for i in range(operation.instruction.removed):
                        a = self.get_stack_args(block_idx)
                        if a is None:
                            a = Output('arg' + str(line.args_needed))
                            line.args_needed += 1
                        in_variables.append(a)
                for i in range(operation.instruction.added):
                    out_variables.append(Output('var' + str(self._symbolIdx)))
                    self._symbolIdx += 1
                # if operation.
                instruction = ContractLine(address=operation.address, assign_to=out_variables,
                                           instruction=operation.instruction, args=in_variables)
                line.add_line(instruction)
                # self._symbolIdx += 1
                instr_idx += 1
            # for swap op codes, we have to wait until after parsing to remove them

            idx = 0
            while idx < len(line.lines):
                if 'SWAP' in line.lines[idx].instruction.name or 'DUP' in line.lines[idx].instruction.name:
                    del line.lines[idx]
                    idx -= 1
                idx += 1
            block_idx += 1
        self.line_blocks[0].name = 'main'
        return self.line_blocks

def main():
    with open('contract.evm', 'r') as contract:
        contract = Contract(contract.read())
        blocks = contract.parse()
        for lines in blocks:
            print(str(lines))
            for line in lines.lines:
                print("\t" * lines.indentation_level + '{1}'.format(hex(line.address), str(line)))
            print()
if __name__ == '__main__':
    main()