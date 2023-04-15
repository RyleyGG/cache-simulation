from Cache import Cache
from SetAssociativeCache import SetAssociativeCache
import pandas

class FullyAssociativeCache(SetAssociativeCache):
    def __init__(self, cache):
        self.totalSize = cache.totalSize
        self.lineBlockSize = cache.lineBlockSize
        self.linesPerSet = cache.linesPerSet
        self.lineNum = cache.lineNum