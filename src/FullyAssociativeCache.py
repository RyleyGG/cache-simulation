from Cache import Cache
from SetAssociativeCache import SetAssociativeCache

class FullyAssociativeCache(SetAssociativeCache):
    def __init__(self, cache):
        self.totalSize = cache.totalSize
        self.lineBlockSize = cache.lineBlockSize
        self.linesPerSet = cache.linesPerSet
        self.lineNum = cache.lineNum
    
    def simulate(self, addrs):
        pass

    def initStruct(self):
        # Fully associative cache has Tag / Offset
        for i in range(0, self.lineNum):
            self.cacheStruct[i] = {
                'set': 0,  # in fully associate caches there is only 1 set
                'tag': '',
                'offset': ''
            }