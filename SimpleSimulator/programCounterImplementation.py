from utilities import intToBinary8bit




class ProgramCounter:
    '''
    Class to model the given scenario of Program Counter
    '''
    currentCounter = 0
    # ........................................................................................................................


    def initialize(self):
        '''
        Function to initialize the Program Counter with a value of 0
        '''
        self.currentCounter = 0
    # ........................................................................................................................
    
    def getValue(self):
        '''
        Function to get the value of the Program Counter
        '''
        return self.currentCounter
    # ........................................................................................................................

    def update(self, newCounter):
        '''
        Function to update the value of the Program Counter to newCounter
        '''
        self.currentCounter = newCounter
    # ........................................................................................................................

    def dump(self):
        '''
        Function to dump the Program Counter onto stdout
        '''
        print(intToBinary8bit(self.currentCounter), end = " ")
    # ........................................................................................................................


PC = ProgramCounter()