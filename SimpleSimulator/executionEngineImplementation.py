from registersImplementation import RF
from memoryImplementation import MEM
from programCounterImplementation import PC
from utilities import checkOverflow, intToBinary8bit, binary8bitToInt

class ExecutionEngine:
    
    def execute(self, instruction):
        '''
        This function takes a 16bit binary string of assembly instructions and returns
        \t(The updated state of the halted instruction, 
        \tThe updated value of the program counter)
        '''
        opcode = instruction[:5:]

        # Append the point for Memory Access Trace
        MEM.xCoordinates.append(MEM.cycle)
        MEM.yCoordinates.append(PC.getValue())
        

        if(opcode == "00000"):
            # add unused reg1 reg2 reg3
            # 5   2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            res = RF.getRegister(reg2, False) + RF.getRegister(reg3, False)
            if(checkOverflow(res)):
                RF.setOverflowFlag()
            RF.setRegister(reg1, res)
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00001"):
            # sub unused reg1 reg2 reg3
            # 5   2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00010"):
            # mov reg1 $Imm
            # 5   3    8
            reg1 = instruction[5:8:]        # reading address of reg1
            value = instruction[8::]        # reading the value of $Imm
            value = binary8bitToInt(value)
            RF.setRegister(reg1, value)
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00011"):
            # mov unused reg1 reg2
            # 5   5      3    3
            reg1 = instruction[10:13:]      # reading the address of reg1
            reg2 = instruction[13::]        # reading the address of reg2
            RF.setRegister(reg1, RF.getRegister(reg2, False))
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00100"):
            # ld reg1 mem_addr
            # 5  3    8
            MEM.xCoordinates.append(MEM.cycle)                          # Appending the point
            MEM.yCoordinates.append(int(instruction[8::], 2))           # of Memory Access
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00101"):
            # st reg1 mem_addr
            # 5  3    8
            MEM.xCoordinates.append(MEM.cycle)                          # Appending the point
            MEM.yCoordinates.append(int(instruction[8::], 2))           # of Memory Access
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00110"):
            # mul unused reg1 reg2 reg3
            # 5   2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00111"):
            # div unused reg3 reg4
            # 5   5      3    3   
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01000"):
            # rs reg1 $Imm
            # 5  3    8
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01001"):
            # ls reg1 $Imm
            # 5  3    8
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01010"):
            # xor unused reg1 reg2 reg3
            # 5   2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01011"):
            # or unused reg1 reg2 reg3
            # 5  2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01100"):
            # and unused reg1 reg2 reg3
            # 5   2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01101"):
            # not unused reg1 reg2
            # 5   5      3    3
            pass
            RF.resetFlagRegister()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01110"):
            # cmp unused reg1 reg2
            # 5   5      3    3
            reg1 = instruction[10:13:]      # reading address of reg1
            reg2 = instruction[13::]        # reading address of reg2

            if RF.getRegister(reg1, False) < RF.getRegister(reg2, False):
                RF.setLessThanFlag()
            elif RF.getRegister(reg1, False) > RF.getRegister(reg2, False):
                RF.setGreaterThanFlag()
            else:
                RF.setEqualsFlag()
            return (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01111"):
            # jmp unused mem_addr
            # 5   3      8
            pass
            RF.resetFlagRegister()
        # ........................................................................................................................

        elif(opcode == "10000"):
            # jlt unused mem_addr
            # 5   3      8
            if RF.flagRegister == "0000000000000100":
                memory = instruction[8::]
                return (False, binary8bitToInt(memory))
            RF.resetFlagRegister()
            
        # ........................................................................................................................

        elif(opcode == "10001"):
            # jgt unused mem_addr
            # 5   3      8
            if RF.flagRegister == "0000000000000010":
                memory = instruction[8::]
                return (False, binary8bitToInt(memory))
            RF.resetFlagRegister()
        # ........................................................................................................................

        elif(opcode == "10010"):
            # je unused mem_addr
            # 5  3      8
            pass
            RF.resetFlagRegister()
        # ........................................................................................................................

        elif(opcode == "10011"):
            # hlt unused
            # 5   11
            RF.resetFlagRegister()
            return (True, PC.getValue() + 1)
        # ........................................................................................................................

        MEM.cycle += 1
        

EE = ExecutionEngine()