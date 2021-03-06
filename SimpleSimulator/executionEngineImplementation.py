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
            else:
                RF.resetFlagRegister()
            RF.setRegister(reg1, res)
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00001"):
            # sub unused reg1 reg2 reg3
            # 5   2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            res = RF.getRegister(reg2,False) - RF.getRegister(reg3,False)
            if (res < 0):
                RF.setOverflowFlag()
                RF.setRegister(reg1,0)
            else:
                RF.setRegister(reg1,res)
                RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00010"):
            # mov reg1 $Imm
            # 5   3    8
            reg1 = instruction[5:8:]        # reading address of reg1
            value = instruction[8::]        # reading the value of $Imm
            value = binary8bitToInt(value)
            RF.setRegister(reg1, value)
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00011"):
            # mov unused reg1 reg2
            # 5   5      3    3
            reg1 = instruction[10:13:]      # reading the address of reg1
            reg2 = instruction[13::]        # reading the address of reg2
            RF.setRegister(reg1, RF.getRegister(reg2, False))
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00100"):
            # ld reg1 mem_addr
            # 5  3    8
            reg1 = instruction[5:8:]
            memoryAddress = instruction[8::]
            MEM.xCoordinates.append(MEM.cycle)                          # Appending the point
            MEM.yCoordinates.append(binary8bitToInt(memoryAddress))     # of Memory Access
            valueAtMemory = MEM.getValueFromAddress(memoryAddress)
            RF.setRegister(reg1, valueAtMemory)
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00101"):
            # st reg1 mem_addr
            # 5  3    8
            reg1 = instruction[5:8:]
            memoryAddress = instruction[8::]
            MEM.xCoordinates.append(MEM.cycle)                          # Appending the point
            MEM.yCoordinates.append(binary8bitToInt(memoryAddress))     # of Memory Access
            MEM.setValueOfAddress(memoryAddress, RF.getRegister(reg1, False))
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00110"):
            # mul unused reg1 reg2 reg3
            # 5   2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            res = RF.getRegister(reg2, False) * RF.getRegister(reg3, False)
            if(checkOverflow(res)):
                RF.setOverflowFlag()
            else:
                RF.resetFlagRegister()
            RF.setRegister(reg1, res)
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "00111"):
            # div unused reg3 reg4
            # 5   5      3    3   
            reg3 = instruction[10:13:]      # Reading address of reg3
            reg4 = instruction[13::]        # Reading address of reg4
            remainder = RF.getRegister(reg3,False) % RF.getRegister(reg4,False)
            quotient = RF.getRegister(reg3,False) // RF.getRegister(reg3,False)
            RF.setRegister("000",quotient)
            RF.setRegister("111",remainder)
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01000"):
            # rs reg1 $Imm
            # 5  3    8
            reg1 = instruction[5:8:]
            immediateValue = binary8bitToInt(instruction[8::])
            shiftedString = '0' * immediateValue + RF.getRegister(reg1, True)[:len(RF.getRegister(reg1, True)) - immediateValue:]
            RF.setRegister(reg1, int(shiftedString, 2))
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01001"):
            # ls reg1 $Imm
            # 5  3    8
            reg1 = instruction[5:8:]
            immediateValue = binary8bitToInt(instruction[8::])
            shiftedString = RF.getRegister(reg1, True)[immediateValue::] + '0' * immediateValue
            RF.setRegister(reg1, int(shiftedString, 2))
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01010"):
            # xor unused reg1 reg2 reg3
            # 5   2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            res = RF.getRegister(reg2,False) ^ RF.getRegister(reg3,False)
            RF.setRegister(reg1,res)
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01011"):
            # or unused reg1 reg2 reg3
            # 5  2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            res = RF.getRegister(reg2,False) | RF.getRegister(reg3,False)
            RF.setRegister(reg1,res)
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01100"):
            # and unused reg1 reg2 reg3
            # 5   2      3    3    3
            reg1 = instruction[ 7:10:]      # reading address of reg1
            reg2 = instruction[10:13:]      # reading address of reg2
            reg3 = instruction[13:16:]      # reading address of reg3
            res = RF.getRegister(reg2,False) & RF.getRegister(reg3,False)
            RF.setRegister(reg1,res)
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01101"):
            # not unused reg1 reg2
            # 5   5      3    3
            reg1 = instruction[10:13:]      # Reading address of reg1
            reg2 = instruction[13::]        # Reading address of reg2
            inverted = ""
            for bit in reg2:
                if bit=='1':
                    inverted += '0'
                else:
                    inverted += '1'
            RF.setRegister(reg1, int(inverted, 2))
            RF.resetFlagRegister()
            (halt, newPC) = (False, PC.getValue() + 1)
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
            (halt, newPC) = (False, PC.getValue() + 1)
        # ........................................................................................................................

        elif(opcode == "01111"):
            # jmp unused mem_addr
            # 5   3      8
            memoryAddress = instruction[8::]
            (halt, newPC) = (False, binary8bitToInt(memoryAddress))
            RF.resetFlagRegister()
        # ........................................................................................................................

        elif(opcode == "10000"):
            # jlt unused mem_addr
            # 5   3      8
            if RF.flagRegister == "0000000000000100":
                memoryAddress = instruction[8::]
                (halt, newPC) = (False, binary8bitToInt(memoryAddress))
            else:
                (halt, newPC) = (False, PC.getValue() + 1)
            RF.resetFlagRegister()
        # ........................................................................................................................

        elif(opcode == "10001"):
            # jgt unused mem_addr
            # 5   3      8
            if RF.flagRegister == "0000000000000010":
                memoryAddress = instruction[8::]
                (halt, newPC) = (False, binary8bitToInt(memoryAddress))
            else:
                (halt, newPC) = (False, PC.getValue() + 1)
            RF.resetFlagRegister()
        # ........................................................................................................................

        elif(opcode == "10010"):
            # je unused mem_addr
            # 5  3      8
            if RF.flagRegister == "0000000000000001":
                memoryAddress = instruction[8::]
                (halt, newPC) = (False, binary8bitToInt(memoryAddress))
            else:
                (halt, newPC) = (False, PC.getValue() + 1)
            RF.resetFlagRegister()
        # ........................................................................................................................

        elif(opcode == "10011"):
            # hlt unused
            # 5   11
            RF.resetFlagRegister()
            (halt, newPC) = (True, PC.getValue() + 1)
        # ........................................................................................................................

        MEM.cycle += 1
        return (halt, newPC)
        

EE = ExecutionEngine()