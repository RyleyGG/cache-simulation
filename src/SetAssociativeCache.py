from Cache import Cache
import pandas

class SetAssociativeCache(Cache):
    replacementPolicy = 0

    def __init__(self, cache):
        self.totalSize = cache.totalSize
        self.lineBlockSize = cache.lineBlockSize
        self.linesPerSet = cache.linesPerSet
        self.lineNum = cache.lineNum
    
    def chooseReplacementPolicy(self):
        replacementMap = {
            '1': 'LRU',
            '2': 'FIFO'
        }
        print('Since your cache is not direct mapped, you must pick a replacement policy. Enter the number corresponding to your choice:')
        print('1) Least Recently Used (LRU)')
        print('2) First in, first out (FIFO)')
        replacementInput = input()

        while replacementInput not in ['1', '2']:
            replacementInput = input(f'"{replacementInput}" is not a valid choice. Enter again: ')
        self.replacementPolicy = replacementMap[replacementInput]