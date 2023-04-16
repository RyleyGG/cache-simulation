from Cache import Cache
import math

class DirectMappedCache(Cache):
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
            curLine = self.addLeadingZeros(binaryStr[self.tagWidth:self.tagWidth + self.lineWidth])
            curOffset = self.addLeadingZeros(binaryStr[self.tagWidth + self.lineWidth:])
            
            itemLine = ''
            if curLine in list(self.hexBinConvMap.values()):
                itemLine = list(self.hexBinConvMap.values()).index(curLine)
            else:
                itemLine = self.binaryToHex(curLine)
            if self.cacheStruct[itemLine]['tag'] == curTag:
                self.hits += 1
            else:
                self.misses += 1
                self.cacheStruct[itemLine] = {
                    'set': self.cacheStruct[itemLine]['set'],
                    'tag': curTag,
                    'offset': curOffset
                }

    def initStruct(self):
        # Direct mapped cache has Tag / Line / Offset
        for i in range(0, self.lineNum):
            self.cacheStruct[i] = {
                'set': i,  # in direct mapped caches each set is one line/block
                'tag': '',
                'offset': ''
            }
        self.offsetWidth = int(math.log2(self.lineBlockSize))
        self.lineWidth = int(math.log2(self.lineNum))
        self.tagWidth = 32 - self.offsetWidth - self.lineWidth