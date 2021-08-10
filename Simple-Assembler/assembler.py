from helper import *
import sys

assemblyCode = []
for line in sys.stdin:
    assemblyCode.append(line)       # ith index of the list represents the (i+1)th line of the assembly code

convertedBinary = []                # append the result statements to be printed in this list
encounteredErrors = []              # append any encountered errors to this list

emptyLines = 0
for line in assemblyCode:
    if(not line):
        emptyLines += 1

haltEncountered = False
labels = dict()
variables = dict()
nextVariableLocation = len(assemblyCode)-emptyLines
variableDeclarationsNow = True

for lineNumber in range(len(assemblyCode)):
    currentLine = assemblyCode[lineNumber].split()
    if(currentLine[0][-1]==":"):
            labels[(currentLine[0][:len(currentLine[0])-1:])] = binary8bit(lineNumber)


for lineNumber in range(len(assemblyCode)):
    if(not assemblyCode[lineNumber]):
        continue
    else:
        currentLine = assemblyCode[lineNumber].split()
        if(currentLine[0]=="var" and variableDeclarationsNow):
            currentLine.pop(0)
            if(len(currentLine)==1):
                variables[currentLine[0]] = binary8bit(nextVariableLocation)
                nextVariableLocation += 1
            else:
                encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Improper variable declaration")
                continue
        elif(currentLine[0]=="var" and not variableDeclarationsNow):
                encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Variable not declared at beginning")
                continue
        elif(currentLine[0]!="var"):
            variableDeclarationsNow = False
        
        if(currentLine[0][-1]==":"):
            currentLine.pop(0)
        


        # -------------------------------------------------------------------------------------------------------
        if(haltEncountered):
            encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Halt(hlt) not being used as the last instruction")
            continue
        # _______________________________________________________________________________________________________


        # -------------------------------------------------------------------------------------------------------
        if(typeOfInstruction(currentLine[0])==-1):
            encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Invalid instruction")
            continue
        # _______________________________________________________________________________________________________


        # -------------------------------------------------------------------------------------------------------
        if(currentLine[0]=="mov" and len(currentLine)==3):
            if(registerAddress(currentLine[2])!=-1):
                # mov reg1 reg2
                temp = opcode(currentLine[0], 1)+"00000"+registerAddress(currentLine[1])+registerAddress(currentLine[2])
                convertedBinary.append(temp)
                continue
            elif(currentLine[2][1::].isdecimal()):
                # mov reg1 $Imm
                temp = opcode(currentLine[0], 0)+registerAddress(currentLine[1])+binary8bit(int(currentLine[2][1::]))
                convertedBinary.append(temp)
                continue
        elif(currentLine[0]=="mov"):
            encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Wrong Syntax used for instruction")
            continue
        # _______________________________________________________________________________________________________


        # -------------------------------------------------------------------------------------------------------
        if(typeOfInstruction(currentLine[0])=='a' and len(currentLine)==4):
            pass
        elif(typeOfInstruction(currentLine[0])=='a'):
            encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Wrong Syntax used for instruction")
            continue
        # _______________________________________________________________________________________________________
        

        # -------------------------------------------------------------------------------------------------------
        if(typeOfInstruction(currentLine[0])=='b' and len(currentLine)==3):
            pass
        elif(typeOfInstruction(currentLine[0])=='b'):
            encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Wrong Syntax used for instruction")
            continue
        # _______________________________________________________________________________________________________
        

        # -------------------------------------------------------------------------------------------------------
        if(typeOfInstruction(currentLine[0])=='c' and len(currentLine)==3):
            pass
        elif(typeOfInstruction(currentLine[0])=='c'):
            encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Wrong Syntax used for instruction")
            continue
        # _______________________________________________________________________________________________________
        

        # -------------------------------------------------------------------------------------------------------
        if(typeOfInstruction(currentLine[0])=='d' and len(currentLine)==3):
            pass
        elif(typeOfInstruction(currentLine[0])=='d'):
            encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Wrong Syntax used for instruction")
            continue
        # _______________________________________________________________________________________________________
        

        # -------------------------------------------------------------------------------------------------------
        if(typeOfInstruction(currentLine[0])=='e' and len(currentLine)==2):
            ins = currentLine.pop(0)
            if(currentLine[0] not in labels.keys()):
                if(currentLine[0] in variables.keys()):
                    encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Misuse of variable as label")
                else:
                    encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+":  Use of undefined labels")
            else:
                convertedBinary.append(opcode(ins)+'0'*3+labels[currentLine[0]])
        elif(typeOfInstruction(currentLine[0])=='e'):
            encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Wrong Syntax used for instruction")
            continue
        # _______________________________________________________________________________________________________
        

        # -------------------------------------------------------------------------------------------------------
        if(typeOfInstruction(currentLine[0])=='f' and len(currentLine)==1):
            convertedBinary.append(opcode(currentLine[0])+'0'*11)
            haltEncountered = True
        elif(typeOfInstruction(currentLine[0])=='f'):
            encounteredErrors.append("ERROR at Line "+str(lineNumber+1)+": Wrong Syntax used for instruction")
            continue
        # _______________________________________________________________________________________________________


if(not haltEncountered):
    encounteredErrors.append("ERROR: No halt(hlt) instruction found")


if(len(encounteredErrors)):
    for error in encounteredErrors:
        print(error)
else:
    for binaryInstruction16bit in convertedBinary:
        print(binaryInstruction16bit)
