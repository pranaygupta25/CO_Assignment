from executionEngineImplementation import EE
from memoryImplementation import MEM
from programCounterImplementation import PC
from registersImplementation import RF


MEM.initialize()
PC.initialize()
halted = False

while(not halted):
    instruction = MEM.getData(PC.getValue())
    halted, newPC = EE.execute(instruction)
    PC.dump()
    RF.dump()
    PC.update(newPC)

MEM.dump()
MEM.plotMemoryAccessTrace()