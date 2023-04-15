from Cache import Cache
from DirectMappedCache import DirectMappedCache
from FullyAssociativeCache import FullyAssociativeCache
from SetAssociativeCache import SetAssociativeCache

def main():
    cache = Cache()
    if cache.linesPerSet == 1:
        print('Based on your input parameters, you have created a direct mapped cache.')
        cache = DirectMappedCache(cache)
    elif cache.linesPerSet == cache.lineNum:
        print('Based on your input parameters, you have created a fully associative cache.')
        cache = FullyAssociativeCache(cache)
        cache.chooseReplacementPolicy()
    else:
        print(f'Based on your input parameters, you have created a {cache.linesPerSet}-associative cache.')
        cache = SetAssociativeCache(cache)
        cache.chooseReplacementPolicy()

if __name__ == '__main__':
    main()