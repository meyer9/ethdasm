"""
Parses opcodes into blocks of simplified opcodes.
"""
import math
from typing import List

import opcodes as oc


class Instruction:
    instruction: oc.OpCode
    address: int
    arguments: List[str]

    def __init__(self, instruction: oc.OpCode, address: int, arguments: List[str]):
        self.instruction = instruction
        self.address = address
        self.arguments = arguments

    def __repr__(self):
        return self.instruction.name


class Block:
    """
    Represents a block of code which can be jumped to within an
    ethereum contract.
    """
    def __init__(self, address):
        self.address = address
        self.instructions = []

    def add_instruction(self, instruction: Instruction):
        """
        Adds an instruction to the block.
        """
        self.instructions.append(instruction)


class ParseException(Exception):
    pass


class Parser:
    """
    Parses EVM code into blocks of optimized code.
    """
    def __init__(self):
        pass

    @staticmethod
    def __parse_ops(contract_code: str) -> List[Instruction]:
        """
        Parse contract code and generates a list of (address, opcode, arguments)
        """
        opcodes = []
        address = 0
        while contract_code:
            offset = 0
            instruction = contract_code[0:2]
            contract_code = contract_code[2:]
            offset += 1
            instr = oc.get_opcode_by_code(instruction)
            args = []
            if instr.args > 0:
                args = [int(contract_code[0:2 * instr.args], 16)]
                contract_code = contract_code[2 * instr.args:]
                offset += instr.args
            opcodes.append(Instruction(instr, address, args))
            address += offset
        return opcodes

    @staticmethod
    def __parse_blocks(instructions: [Instruction]) -> [Block]:
        """
        Parses contract code and generates a list of blocks which contain
        opcodes within the block.
        """
        blocks = []
        current_block = Block(instructions[0].address)
        for operation in instructions:
            if operation.instruction.name == 'JUMPDEST':
                blocks.append(current_block)
                current_block = Block(operation.address)
            current_block.add_instruction(operation)
        if len(blocks) == 0:
            blocks.append(current_block)
        return blocks

    @staticmethod
    def __optimize_jump_args(instructions: [Instruction]) -> [Instruction]:
        i = 0
        while i < len(instructions) - 2:
            if 'PUSH' in instructions[i].instruction.name:
                if 'JUMP' == instructions[i + 1].instruction.name:
                    instructions[i + 1].arguments = instructions[i].arguments
                    del instructions[i]
                elif 'PUSH' in instructions[i + 1].instruction.name and 'JUMPI' == instructions[i + 2].instruction.name:
                    instructions[i + 1].arguments = instructions[i].arguments + instructions[i + 1].arguments
                    del instructions[i]
                    del instructions[i + 1]
            i += 1
        return instructions

    @staticmethod
    def __optimize(instructions: [Instruction]) -> [Instruction]:
        Parser.__optimize_jump_args(instructions)
        last_len = len(instructions) + 1
        while last_len > len(instructions):
            last_len = len(instructions)
            Parser.__optimize_arguments(instructions)
            Parser.__optimize_math(instructions)
        Parser.__optimize_arguments(instructions)
        return instructions

    @staticmethod
    def parse(contract_code: str) -> [Block]:
        """
        Parses contract code into a list of blocks.
        """
        opcodes = Parser.__parse_ops(contract_code)
        optimized_opcodes = Parser.__optimize(opcodes)
        blocks = Parser.__parse_blocks(optimized_opcodes)
        return blocks

    @staticmethod
    def __optimize_arguments(instructions: [Instruction]) -> [Instruction]:
        """
        Removes calls with preceding pushes and adds a list of arguments to them instead.
        """
        i = 0
        while i < len(instructions):
            num_pushes = instructions[i].instruction.removed
            args = []
            not_static = num_pushes == 0
            if len(instructions[i].arguments) > 0:
                not_static = True
                num_pushes = 0
            if 'DUP' in instructions[i].instruction.name or 'SWAP' in instructions[i].instruction.name:
                i += 1
                continue
            if i - num_pushes < 0:
                break
            for push_num in range(i - num_pushes, i):
                not_static = not_static or 'PUSH' not in instructions[push_num].instruction.name
            if not_static:
                i += 1
                continue
            for push_num in range(num_pushes):
                args.append(instructions[i-push_num-1].arguments[0])
                del instructions[i-push_num-1]
            if not not_static:
                instructions[i - num_pushes].arguments = args
            i += 1
        return instructions

    @staticmethod
    def __get_num_bytes(num: int):
        return math.ceil(math.log(num) / 8)

    @staticmethod
    def __optimize_math(instructions: [Instruction]) -> [Instruction]:
        i = 0
        while i < len(instructions):
            equiv_func = instructions[i].instruction.equivalent_function
            if instructions[i].arguments and equiv_func and len(instructions[i].arguments) == instructions[i].instruction.removed:
                print(instructions[i].arguments)
                equiv = equiv_func(*instructions[i].arguments)
                push_num = int(min(Parser.__get_num_bytes(equiv), 31))
                op_code = hex(int('60', 16) + push_num)[2:]
                instructions[i] = Instruction(oc.get_opcode_by_code(op_code), instructions[i].address, [equiv])
            i += 1
        return instructions
