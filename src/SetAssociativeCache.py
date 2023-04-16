from Cache import Cache
import math

class SetAssociativeCache(Cache):
    replacementPolicy = ''
    lruCounter = 1
    fifoCounter = 1

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
    
    def simulate(self, addrs):
        for addr in addrs:
            binaryStr = ''
            for char in addr:
                binaryStr += self.hexBinConvMap[char]
            
            curTag = self.addLeadingZeros(binaryStr[0:self.tagWidth])
            curSet = self.addLeadingZeros(binaryStr[self.tagWidth:self.tagWidth + self.setWidth])
            curOffset = self.addLeadingZeros(binaryStr[self.tagWidth + self.setWidth:])
            
            # in set associative caches, we can get the relevant indices by linesPerSet * curSet
            # range is  [linesPerSet * curSet, (linesPerSet * curSet) + linesPerSet
            itemSet = 0
            if curSet in list(self.hexBinConvMap.values()):
                itemSet = list(self.hexBinConvMap.values()).index(curSet)
            else:
                itemSet = self.binaryToHex(curSet)

            foundIndex = None
            itemFound = False
            lineIter = self.linesPerSet * int(itemSet)
            while lineIter <= self.linesPerSet * int(itemSet) + self.linesPerSet - 1:
                if self.cacheStruct[lineIter]['tag'] == curTag:
                    itemFound = True
                    foundIndex = lineIter
                    break
                lineIter += 1

            if itemFound:
                self.hits += 1
                self.cacheStruct[foundIndex]['lru_counter'] = self.lruCounter
                self.lruCounter += 1
            else:
                self.misses += 1
                emptyFound = False
                lineIter = self.linesPerSet * int(itemSet)
                while lineIter <= self.linesPerSet * int(itemSet) + self.linesPerSet - 1:
                    if self.cacheStruct[lineIter]['tag'] == '':
                        emptyFound = True
                        self.cacheStruct[lineIter] = {
                            'set': int(itemSet),
                            'tag': curTag,
                            'offset': curOffset,
                            'lru_counter': self.lruCounter,
                            'fifo_counter': self.fifoCounter
                        }
                        self.lruCounter += 1
                        self.fifoCounter += 1
                        break
                    lineIter += 1

                if not emptyFound:
                    counterStr = ''
                    if self.replacementPolicy == 'LRU':
                        counterStr = 'lru_counter'
                    elif self.replacementPolicy == 'FIFO':
                        counterStr = 'fifo_counter'
                    else:
                        print('No replacement strategy set. Exiting...')
                        exit(1)
                    lineIter = self.linesPerSet * int(itemSet)
                    replaceIndex = lineIter
                    oldestCounter = self.cacheStruct[replaceIndex][counterStr]
                    while lineIter <= self.linesPerSet * int(itemSet) + self.linesPerSet - 1:
                        if self.cacheStruct[lineIter][counterStr] < oldestCounter:
                            replaceIndex = lineIter
                            oldestCounter = self.cacheStruct[lineIter][counterStr]
                        lineIter += 1
                    self.cacheStruct[replaceIndex] = {
                        'set': int(itemSet),
                        'tag': curTag,
                        'offset': curOffset,
                        'lru_counter': self.lruCounter,
                        'fifo_counter': self.fifoCounter
                    }
                    self.lruCounter += 1
                    self.fifoCounter += 1

    def initStruct(self):
        # Set-associative cache has Tag / Set / Offset
        setNum = 0
        lineIter = 0
        for i in range(0, self.lineNum):
            if lineIter == self.linesPerSet:
                setNum += 1
                lineIter = 0
            self.cacheStruct[i] = {
                'set': setNum,  # in set-associative caches the set number is dependent on other size factors
                'tag': '',
                'offset': '',
                'lru_counter': 0,
                'fifo_counter': 0
            }
            lineIter += 1
        self.offsetWidth = int(math.log2(self.lineBlockSize))
        self.setWidth = int(math.log2(self.lineNum / self.linesPerSet))
        self.tagWidth = 32 - self.offsetWidth - self.setWidth