from Cache import Cache
from DirectMappedCache import DirectMappedCache
from FullyAssociativeCache import FullyAssociativeCache
from SetAssociativeCache import SetAssociativeCache
import glob
import os

def main():
    cache = Cache()
    cwd = os.getcwd().split('/src')[0].split('\src')[0]
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
    cache.initStruct()

    print('Importing test data...')
    allTestFiles = {}
    for item in glob.glob(f'{cwd}/tests/*.trace'):
        fileAddrs = []
        with open(item, 'r') as file:
            for line in file:
                addr = line.split(' ')[1][2:].lower()
                fileAddrs.append(addr)
        allTestFiles[item.replace('\\', '/').split('tests/')[1]] = fileAddrs
    for file, addrs in allTestFiles.items():
        print(f'Cycling addresses from {file}')
        cache.simulate(addrs)
    print(f'There were {cache.hits} hits and {cache.misses} misses. This is a {round((cache.hits / (cache.hits + cache.misses)) * 100, 2)}% hit rate.')

if __name__ == '__main__':
    main()