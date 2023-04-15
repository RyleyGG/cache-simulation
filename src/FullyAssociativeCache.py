from Cache import Cache
import pandas

class FullyAssociativeCache(Cache):
    def __init__(self, cache):
        self.totalSize = cache.totalSize
        self.lineBlockSize = cache.lineBlockSize
        self.linesPerSet = cache.linesPerSet
        self.lineNum = cache.lineNum