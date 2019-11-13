"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.registers = [0]*8
        self.ir = 0
        self.pc = 0

    def ram_read(self, index):
        return self.ram[index]

    def ram_write(self, index, value):
        self.ram[index] = value

    def load(self, program):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111,  # PRN R0
        #     0b00000000,
        #     0b10100010,  # MUL
        #     0b00000001,  # HLT
        # ]

        with open(program) as f:
            for line in f:
                line = line.split("#")[0]
                line = line.strip()
                if line == '':
                    continue
                # print(f'Line in ls8.py: {line}')
                val = int(line, 2)
                print(f'val:{val}')
                self.ram[address] = val
                address += 1

        # for instruction in program:

            # print(self.ram)
            # val = int(instruction, 2)
            # print(val)
            # memory[address] = val
            # address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.registers[reg_a] += self.registers[reg_b]
        elif op == "MUL":
            self.registers[reg_a] *= self.registers[reg_b]

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        HALT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        MUL = 0b10100010

        self.pc = 0
        running = True
        while running is True:
            # print(self.ram)
            self.ir = self.ram[self.pc]
            operand_a = self.ram[self.pc+1]
            operand_b = self.ram[self.pc+2]
            # HLT Halt
            if self.ir == HALT:
                break
            # LDI Store value in register  reg, val
            elif self.ir == LDI:
                # print(f'LDI:{operand_b}')
                self.registers[operand_a] = operand_b
                self.pc += 3
            # PRN Print
            elif self.ir == PRN:
                print(f'PRN:{self.registers[operand_a]}')
                self.pc += 2
            # MUL multiply
            elif self.ir == MUL:
                self.alu("MUL", operand_a, operand_b)
                self.pc += 3
            else:
                self.pc += 1
