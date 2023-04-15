import pandas
import math

class Cache:
    totalSize = 0
    lineBlockSize = 0
    linesPerSet = 0
    lineNum = 0

    def __init__(self):
        self.totalSize = input('Enter total number of bytes to be stored in the cache. Use a power of 2: ')
        validInput = self.validParam(self.totalSize, True)
        while not validInput:
            self.totalSize = input(f'"{self.totalSize}" is not a valid power of 2. Enter again: ')
            validInput = self.validParam(self.totalSize, True)
        self.totalSize = int(self.totalSize)

        self.lineBlockSize = input('Enter the number of bytes in a block / line. Use a power of 2: ')
        validInput = self.validParam(self.lineBlockSize, True)
        while not validInput:
            self.lineBlockSize = input(f'"{self.lineBlockSize}" is not a valid power of 2. Enter again: ')
            validInput = self.validParam(self.lineBlockSize, True)
        self.lineBlockSize = int(self.lineBlockSize)

        self.linesPerSet = input('Enter the number of lines per set: ')
        validInput = self.validParam(self.linesPerSet, False)
        while not validInput:
            self.linesPerSet = input(f'"{self.linesPerSet}" is not a valid value. Enter again: ')
            validInput = self.validParam(self.linesPerSet, False)
        self.linesPerSet = int(self.linesPerSet)

        self.lineNum = int(self.totalSize / self.lineBlockSize)
        print(f'Based on your input parameters, the number of lines in the cache is: {self.lineNum}')
    
    def validParam(self, value, powerTwoCheck):
        try:
            value = int(value)
            if powerTwoCheck:
                if math.log2(value).is_integer():
                    return True
            else:
                return True
        except ValueError:
            pass
        return False