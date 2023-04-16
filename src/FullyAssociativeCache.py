from SetAssociativeCache import SetAssociativeCache
import math

class FullyAssociativeCache(SetAssociativeCache):
    def __init__(self, cache):
        self.totalSize = cache.totalSize
        self.lineBlockSize = cache.lineBlockSize
        self.linesPerSet = cache.linesPerSet
        self.lineNum = cache.lineNum
    
    def simulate(self, addrs):
        for addr in addrs:
            binaryStr = ''
            for char in addr:
                binaryStr += self.hexBinConvMap[char]
            
            curTag = self.addLeadingZeros(binaryStr[0:self.tagWidth])
            curOffset = self.addLeadingZeros(binaryStr[self.tagWidth + self.setWidth:])
            
            # in set associative caches, we can get the relevant indices by linesPerSet * curSet
            # range is  [linesPerSet * curSet, (linesPerSet * curSet) + linesPerSet]
            foundIndex = None
            itemFound = False
            lineIter = 0
            while lineIter < self.lineNum:
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
                lineIter = 0
                while lineIter < self.lineNum:
                    if self.cacheStruct[lineIter]['tag'] == '':
                        emptyFound = True
                        self.cacheStruct[lineIter] = {
                            'set': 0,
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
                    lineIter = 0
                    replaceIndex = lineIter
                    oldestCounter = self.cacheStruct[replaceIndex][counterStr]
                    while lineIter < self.lineNum:
                        if self.cacheStruct[lineIter][counterStr] < oldestCounter:
                            replaceIndex = lineIter
                            oldestCounter = self.cacheStruct[lineIter][counterStr]
                        lineIter += 1
                    self.cacheStruct[replaceIndex] = {
                        'set': 0,
                        'tag': curTag,
                        'offset': curOffset,
                        'lru_counter': self.lruCounter,
                        'fifo_counter': self.fifoCounter
                    }
                    self.lruCounter += 1
                    self.fifoCounter += 1

    def initStruct(self):
        # Fully associative cache has Tag / Offset
        for i in range(0, self.lineNum):
            self.cacheStruct[i] = {
                'set': 0,  # in fully associate caches there is only 1 set
                'tag': '',
                'offset': '',
                'lru_counter': 0,
                'fifo_counter': 0
            }
        self.offsetWidth = int(math.log2(self.lineBlockSize))
        self.tagWidth = 32 - self.offsetWidth