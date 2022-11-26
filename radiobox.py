

class ALU:
    def __init__(self) -> None:
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def inc(self, a):
        return a + 1

    def dec(self, a):
        return a - 1


class Register:
    
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name} = {self.value}"

    def __repr__(self) -> str:
        return f"{self.name} = {self.value}"

def validater(instruction):
    global opCodes
    global registers

    print("This is working")
    print(opCodes)
    print(registers)

    if instruction[0] in opCodes:
        if instruction[1] in registers:
            if instruction[2] in registers:
                print("Valid")
    else:
        print("Invalid")


def instructionParser(instruction):
    tokens = instruction.split(" ")
    tokens[1] = tokens[1].replace(",", "")
    validater(tokens)


eax = Register("eax", 0)
ebx = Register("ebx", 0)
ecx = Register("ecx", 0)
edx = Register("edx", 0)


registers = ["eax", "ebx", "ecx", "edx"]
opCodes = ["add", "sub", "mul", "div", "inc", "dec"]

print("Welcome to the Intel 8086 Simulator\n\n")
print("Instructions:\n")
print("Available registers: eax, ebx, ecx, edx\n")
print("Available opcodes: add, sub, mul, div, inc, dec\n")
print("Enter the instruction in the following format: opcode register1 register2\n")
print("Example: add eax, ebx\n")
instruction = input("[Enter]");
instructionParser(instruction)

