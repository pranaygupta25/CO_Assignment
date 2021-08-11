from helper import *
import sys

assemblyCode = []
for line in sys.stdin:
    if(line):
        assemblyCode.append(line)  # ith index of the list represents the (i+1)th line of the assembly code

convertedBinary = []  # append the result statements to be printed in this list
encounteredErrors = []  # append any encountered errors to this list


haltEncountered = False
labels = dict()
variables = dict()
variableDeclarationsNow = True

varLines = 0
for line in assemblyCode:
    if(line.split()[0] == "var"):
        varLines += 1
    else:
        break

nextVariableLocation = len(assemblyCode) - varLines
while(varLines):
    line = assemblyCode[0].split()
    if(line[0] == "var" and len(line) == 2):
        variables[line[1]] = binary8bit(nextVariableLocation)
        nextVariableLocation += 1
        varLines -= 1
        assemblyCode.pop(0)
        continue
    elif(line[0] == "var"):
        encounteredErrors.append("ERROR: Improper variable declaration")
        varLines -= 1
        assemblyCode.pop(0)
        continue
    else:
        variableDeclarationsNow = False
        break
variableDeclarationsNow = False



for lineNumber in range(len(assemblyCode)):
    currentLine = assemblyCode[lineNumber].split()
    if (assemblyCode[lineNumber].split()[0][-1] == ":"):
        labels[(assemblyCode[lineNumber].split()[0][:len(assemblyCode[lineNumber].split()[0]) - 1:])] = binary8bit(lineNumber)
        temp = ""
        for i in range(1,len(assemblyCode[lineNumber].split())):
            temp += assemblyCode[lineNumber].split()[i] + " "
        assemblyCode[lineNumber] = temp

for lineNumber in range(len(assemblyCode)):


    currentLine = assemblyCode[lineNumber].split()
    if (not currentLine):
        continue
    if (currentLine[0] == "var" and not variableDeclarationsNow):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Variable not declared at beginning")
        continue
    if (currentLine[0][-1] == ":"):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Use of multiple labels is not supported")
        continue


    # -------------------------------------------------------------------------------------------------------
    if (haltEncountered):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Halt(hlt) not being used as the last instruction")
        continue
    # _______________________________________________________________________________________________________

    # -------------------------------------------------------------------------------------------------------
    if (typeOfInstruction(currentLine[0]) == -1 and currentLine[0] != "mov"):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Invalid instruction")
        continue
    # _______________________________________________________________________________________________________

    # -------------------------------------------------------------------------------------------------------
    if (currentLine[0] == "mov" and len(currentLine) == 3):
        if (registerAddress(currentLine[2]) != -1):
            # mov reg1 reg2
            if (registerAddress(currentLine[1]) == -1 or registerAddress(currentLine[2]) == -1):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Invalid Register")
                continue
            if(registerAddress(currentLine[1]) == "111"):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Illegal use of FLAGS")
                continue
            convertedBinary.append(opcode(currentLine[0], 1) + "00000" + registerAddress(currentLine[1]) + registerAddress(currentLine[2]))
            continue
        elif (currentLine[2][1::].isdecimal()):
            # mov reg1 $Imm
            if (registerAddress(currentLine[1]) == -1):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Invalid Register")
                continue
            if(registerAddress(currentLine[1]) == "111"):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Illegal use of FLAGS")
                continue
            if (int(currentLine[2][1::]) < 0 or int(currentLine[2][1::]) > 255):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Illegal Immediate Value")
                continue
            convertedBinary.append(opcode(currentLine[0], 0) + registerAddress(currentLine[1]) + binary8bit(int(currentLine[2][1::])))
            continue
    elif (currentLine[0] == "mov"):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Wrong Syntax used for instruction")
        continue
    # _______________________________________________________________________________________________________

    # -------------------------------------------------------------------------------------------------------
    if (typeOfInstruction(currentLine[0]) == 'a' and len(currentLine) == 4):
        if (registerAddress(currentLine[1]) == -1 or registerAddress(currentLine[2]) == -1 or registerAddress(currentLine[3]) == -1):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Invalid Register")
                continue
        if (registerAddress(currentLine[1]) == "111" or registerAddress(currentLine[2]) == "111" or registerAddress(currentLine[3]) == "111"):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Illegal use of FLAGS")
                continue
        convertedBinary.append(opcode(currentLine[0]) + "00" + registerAddress(currentLine[1]) + registerAddress(currentLine[2]) + registerAddress(currentLine[3]))
        continue
    elif (typeOfInstruction(currentLine[0]) == 'a'):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Wrong Syntax used for instruction")
        continue
    # _______________________________________________________________________________________________________

    # -------------------------------------------------------------------------------------------------------
    if (typeOfInstruction(currentLine[0]) == 'b' and len(currentLine) == 3):
        if(int(currentLine[2][1::]) not in range(0,256)):
            encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Illegal Immediate Value")
            continue
        if(registerAddress(currentLine[1])==-1):
            encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Invalid Register")
            continue
        if(registerAddress(currentLine[1]) == "111"):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Illegal use of FLAGS")
                continue
        convertedBinary.append((opcode(currentLine[0]) + registerAddress(currentLine[1]) + binary8bit(int(currentLine[2][1::]))))
        continue
    elif(typeOfInstruction(currentLine[0]) == 'b'):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Wrong Syntax used for instruction")
        continue
    # _______________________________________________________________________________________________________

    # -------------------------------------------------------------------------------------------------------
    if (typeOfInstruction(currentLine[0]) == 'c' and len(currentLine) == 3):
        if (registerAddress(currentLine[1]) == -1 or registerAddress(currentLine[2]) == -1):
            encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Invalid Register")
            continue
        if(registerAddress(currentLine[1]) == "111" or registerAddress(currentLine[2]) == "111"):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Illegal use of FLAGS")
                continue
        convertedBinary.append(opcode(currentLine[0]) + "00000" + registerAddress(currentLine[1]) + registerAddress(currentLine[2]))
        continue
    elif (typeOfInstruction(currentLine[0]) == 'c'):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Wrong Syntax used for instruction")
        continue
    # _______________________________________________________________________________________________________

    # -------------------------------------------------------------------------------------------------------
    if (typeOfInstruction(currentLine[0]) == 'd' and len(currentLine) == 3):
        if (registerAddress(currentLine[1]) == -1):
            encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Invalid Register")
            continue
        if(registerAddress(currentLine[1]) == "111"):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Illegal use of FLAGS")
                continue
        if (currentLine[2] not in variables.keys()):
            if(currentLine[2] in labels.keys()):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Misuse of label as variable")
                continue
            else:
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Use of undefined variable")
                continue
        else:
            convertedBinary.append(opcode(currentLine[0]) + registerAddress(currentLine[1]) + variables[currentLine[2]])
            continue
    elif (typeOfInstruction(currentLine[0]) == 'd'):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Wrong Syntax used for instruction")
        continue
    # _______________________________________________________________________________________________________

    # -------------------------------------------------------------------------------------------------------
    if (typeOfInstruction(currentLine[0]) == 'e' and len(currentLine) == 2):
        ins = currentLine.pop(0)
        if (currentLine[0] not in labels.keys()):
            if (currentLine[0] in variables.keys()):
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Misuse of variable as label")
                continue
            else:
                encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Use of undefined labels")
                continue
        else:
            convertedBinary.append(opcode(ins) + '0' * 3 + labels[currentLine[0]])
            continue
    elif (typeOfInstruction(currentLine[0]) == 'e'):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Wrong Syntax used for instruction")
        continue
    # _______________________________________________________________________________________________________

    # -------------------------------------------------------------------------------------------------------
    if (typeOfInstruction(currentLine[0]) == 'f' and len(currentLine) == 1):
        convertedBinary.append(opcode(currentLine[0]) + '0' * 11)
        haltEncountered = True
        continue
    elif (typeOfInstruction(currentLine[0]) == 'f'):
        encounteredErrors.append("ERROR at Line " + str(lineNumber + 1) + ": Wrong Syntax used for instruction")
        continue
    # _______________________________________________________________________________________________________

if (not haltEncountered):
    encounteredErrors.append("ERROR: No halt(hlt) instruction found")

if (len(encounteredErrors)):
    for error in encounteredErrors:
        print(error)
else:
    for binaryInstruction16bit in convertedBinary:
        print(binaryInstruction16bit)
