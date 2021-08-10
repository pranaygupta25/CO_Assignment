from helper import *
import sys

assemblyCode = []
for line in sys.stdin:
    assemblyCode.append(line)       # ith index of the list represents the (i+1)th line of the assembly code

convertedBinary = []                # append the result statements to be printed in this list
encounteredErrors = []              # append any encountered errors to this list


















if(len(encounteredErrors)):
    for error in encounteredErrors:
        print(error)
else:
    for binaryInstruction16bit in convertedBinary:
        print(binaryInstruction16bit)
