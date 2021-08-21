from utilities import checkOverflow, intToBinary16bit




class Registers:
    '''
    Class to model the given scenario of registers (R0-R6 and FLAGS)
    '''
    registers = {
                    "000": 0,               # R0
                    "001": 0,               # R1
                    "010": 0,               # R2
                    "011": 0,               # R3
                    "100": 0,               # R4
                    "101": 0,               # R5
                    "110": 0,               # R6
                }
    flagRegister = "0000000000000000"       # FLAGS
    # ........................................................................................................................

    
    def resetFlagRegister(self):
        '''
        Resests the state of the Flag Register to the default value of all unset bits\n
        To be used after every instruction.
        '''
        self.flagRegister = "0000000000000000"
    # ........................................................................................................................

    def setOverflowFlag(self):
        '''
        Sets the Overflow(V) flag: 3rd bit to 1\n
        This flag is set by add, sub and mul, when the result of the operation overflows.
        '''
        self.flagRegister = "0000000000001000"
    # ........................................................................................................................

    def setLessThanFlag(self):
        '''
        Sets the Less Than(L) flag: 2nd bit to 1\n
        This flag is set by the "cmp reg1 reg2" instruction if reg1 < reg2
        '''
        self.flagRegister = "0000000000000100"
    # ........................................................................................................................

    def setGreaterThanFlag(self):
        '''
        Sets the Greater Than(G) flag: 1st bit to 1\n
        This flag is set by the "cmp reg1 reg2" instruction if the value of reg1 > reg2
        '''
        self.flagRegister = "0000000000000010"
    # ........................................................................................................................

    def setEqualsFlag(self):
        '''
        Sets the Equals(G) flag: 0th bit to 1\n
        This flag is set by the "cmp reg1 reg2" instruction if reg1 = reg2
        '''
        self.flagRegister = "0000000000000001"
    # ........................................................................................................................

    def printFlag(self):
        '''
        Prints the current value stored in the flag register\n
        This is used when dumping the current status of the flag register during every cycle
        '''
        print(self.flagRegister, end=" ")
    # ........................................................................................................................
    
    def setRegister(self, registerAddress, value):
        '''
        Sets the value of the register with the address "registerAddress" to the value contained in "value"
        \tregisterAddress: 3bit Binary String containing the address of the register being referred to
        \tvalue: int value to be stored in the register
        '''
        if(not checkOverflow(value)):
            self.registers[registerAddress] = value
        else:
            rawBinary = bin(value)[2::]
            self.registers[registerAddress] = int(rawBinary[len(rawBinary)-16::], 2)
    # ........................................................................................................................
    
    def getRegister(self, registerAddress, binaryOrDecimal):
        '''
        Returns the value stored in the register with the address "registerAddress"
        \tbinaryOrDecimal: boolean to decide if the return value has to be a 16bit binary string or a int value
        \t\tif(binaryOrDecimal= True) => 16bit binary string\n
        \t\tif(binaryOrDecimal= False) => int
        '''
        if(binaryOrDecimal):
            if(registerAddress == "111"):
                return self.flagRegister
            rawBinary = bin(self.registers[registerAddress])[2::]
            if(len(rawBinary)>16):
                return rawBinary[len(rawBinary)-16::]
            else:
                return intToBinary16bit(self.registers[registerAddress])
        else:
            if(registerAddress == "111"):
                return int(self.flagRegister, 2)
            return self.registers[registerAddress]
    # ........................................................................................................................

    def dump(self):
        '''
        Function to dump the values stored in the Registers to stdout
        '''
        for key in self.registers.keys():
            print(intToBinary16bit(self.registers[key]), end = " ")
        print(self.flagRegister)
    # ........................................................................................................................


RF = Registers()