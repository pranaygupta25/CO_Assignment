'''
This file contains helper functions, dictionaries and other resources that might be helpful for the assembler
'''


def binary8bit(number):
    '''
    Returns a string of the 8bit representation of the number (includes 0 if less than 8bits are sufficient for the representation)\n
    number: A whole number in the inclusive range of 0 and 255
    '''
    binaryEquivalent = bin(number)[2::]
    res = '0'*(8-len(binaryEquivalent))+binaryEquivalent
    return res


def opcode(ins, isRegister= -1):
    '''
    Returns a string of the opcode of the instruction passed as a parameter\n
    ins: The syntactical instruction. For example, mul for multiply instruction\n
    In case of MOV instruction, isRegister= 0 for immediate and isRegister= 1 for register\n
    Do not pass the second argument for other commands. 
    '''
    opcodeTable={ 
                    "add": "00000",
                    "sub": "00001",
                    "mov": ["00010", "00011"],      #immediate and register cases respectively
                    "ld" : "00100",
                    "st" : "00101",
                    "mul": "00110",
                    "div": "00111",
                    "rs" : "01000",
                    "ls" : "01001",
                    "xor": "01010",
                    "or" : "01011",
                    "and": "01100",
                    "not": "01101",
                    "cmp": "01110",
                    "jmp": "01111",
                    "jlt": "10000",
                    "jgt": "10001",
                    "je" : "10010",
                    "hlt": "10011"
                }
    if(isRegister == 0):
        return opcodeTable["mov"][0]
    elif(isRegister == 1):
        return opcodeTable["mov"][1]
    return opcodeTable[ins]
        

def typeOfInstruction(ins, isRegister= -1):
    '''
    Returns a string from {'a', 'b', 'c', 'd', 'e', 'f'} depending on the type of the instruction passed as a parameter\n
    If the instruction is not part of the ISA, the function returns -1
    ins: The syntactical instruction. For example, mul for multiply instruction
    In case of MOV instruction, isRegister= 0 for immediate and isRegister= 1 for register\n
    Do not pass the second argument for other commands.
    '''
    type=   {
                'a': ["add", "sub", "mul", "xor", "or", "and"],
                'b': ["mov", "rs", "ls"],
                'c': ["mov", "div", "not", "cmp"],
                'd': ["ld", "st"],
                'e': ["jmp", "jlt", "jgt", "je"],
                'f': ["hlt"]
            } 
    if(isRegister==0):
        return 'b'
    if(isRegister==1):
        return 'c'
    for i in type.keys():
        if ins in type[i]:
            return i
    return -1


def registerAddress(register):
    '''
    Returns a string of 3bit representation of the address the specified register.\n
    register: a string containing the name of the register. Use uppercase alphabets only.
    Returns -1 in case of an invalid register
    '''
    registers = {
                    'R0': '000',
                    'R1': '001',
                    'R2': '010',
                    'R3': '011',
                    'R4': '100',
                    'R5': '101',
                    'R6': '110',
                    'FLAGS': '111'
                }
    if(register in registers.keys()):
        return registers[register]
    return -1
