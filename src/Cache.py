import pandas
import math

class Cache:
    totalSize = 0
    lineBlockSize = 0
    linesPerSet = 0
    lineNum = 0
    hits = 0
    misses = 0
    tagWidth = 0
    lineWidth = 0
    offsetWidth = 0
    setWidth = 0
    cacheStruct = {}
    hexBinConvMap = { # Very inelegant solution btu since we don't need to do any arithmetic, only matching,  it'll work
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111'
    }
    hexDecConvMap = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

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

    def addLeadingZeros(self, inputStr):
        newStr = inputStr
        while len(newStr) % 4 != 0:
            newStr = '0' + newStr
        return newStr

    def binaryToHex(self, inputStr):
        outputVal = 0
        newStr = ''
        iters = 0
        for char in inputStr:
            if len(newStr) != 4:
                newStr += char
            else:
                hexChar = list(self.hexBinConvMap.values()).index(newStr)
                decInt = 0
                if hexChar not in self.hexDecConvMap:
                    decInt = int(hexChar)
                else:
                    decInt = self.hexDecConvMap[hexChar]
                outputVal += decInt * (10**iters)
                iters += 1
                newStr = ''

        return outputVal

    def simulate(self, addrs):
        pass

    def initStruct(self):
        pass