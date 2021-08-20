




def intToBinary16bit(value):
    '''
    Returns a 16bit string of the binary value of the parameter.
    '''
    rawBinary = bin(value)[2::]
    length = len(rawBinary)
    binary = '0' * (16 - length) + rawBinary
    return binary
# ........................................................................................................................

def intToBinary8bit(value):
    '''
    Exclusively used for Program Counnter (PC)
    '''
    rawBinary = bin(value)[2::]
    length = len(rawBinary)
    binary = '0' * (8 - length) + rawBinary
    return binary
# ........................................................................................................................
    
def binary8bitToInt(binaryValue):
    '''
    Converts 8bit binary strings to their respective integer values
    '''
    return int(binaryValue, 2)
# ........................................................................................................................

def checkOverflow(value):
    '''
    Checks if the value exceeds the range of the registers or not i.e. is it greater than (2^16-1)
    \n\tvalue: An integer value to be passed. The value stored in the register
    \n\tReturns a boolean: True-> overflow      False-> No Overflow
    '''
    if(value > (2**16 - 1)):
        return True
    else:
        return False
# ........................................................................................................................