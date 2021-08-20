from sys import stdin




class Memory:
    '''
    Class to model the given scenario of Memory
    '''
    mem = []                        # Input Binary
    xCoordinates = []
    yCoordinates = []
    cycle = 0
    # ........................................................................................................................


    def initialize(self):
        '''
        Function to load all the lines from stdin to memory 
        '''
        for line in stdin:
            self.mem.append(line[0:16:])
        if(len(self.mem)<256):
            lineDifference = 256 - len(self.mem)
            while(lineDifference):
                self.mem.append("0000000000000000")
                lineDifference -= 1
    # ........................................................................................................................
    
    def getData(self, currentPC):
        '''
        Function to return the instruction present at the (currentPC)th line of the memory
        '''
        return self.mem[currentPC]
    # ........................................................................................................................

    def dump(self):
        '''
        Function to dump the memory onto stdout
        '''
        for ins in self.mem:
            print(ins)
    # ........................................................................................................................

    def plotMemoryAccessTrace(self):
        '''
        Function to plot the graph of Memory Access Trace as a png called "memoryAccessTrace.png"
        '''
        import matplotlib.pyplot as plt
        plt.style.use('dark_background')
        plt.scatter(self.xCoordinates, self.yCoordinates, c="#3fada8")
        plt.ylabel("Memory Address")
        plt.xlabel("Cycle Number")
        plt.savefig('memoryAccessTrace.png')
    # ........................................................................................................................


MEM = Memory()