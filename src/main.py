import argparse
from listdir import listdir
from check import check
from setDirs import setHome, setExt
from bloomfilter import BloomFilter
from sync import moveLocaltoExt

# tabnanny.check("/bloomsync")

check()

bloomFilterClient: BloomFilter = BloomFilter()

bloomParser = argparse.ArgumentParser(description="Sync contents of two independent directories.")
bloomParser.add_argument("-ls", "--listdir", dest="path", help="list the contents of a directory.")
bloomParser.add_argument("-l", "--local", dest="localPath", help="sets home directory.")
bloomParser.add_argument("-e", "--ext", dest="extPath", help="sets external directory.")
bloomParser.add_argument("-S", "--sync", dest="sync", help="sync files between directories.")
bloomParser.add_argument("-a", "--all", dest="all", help="iterate through all files, including hidden ones.", action="store_true", default=False)
bloomParser.add_argument("-v", "--verbose", dest="verbose", help="perform operations verbosely.", action="store_true", default=False)
bloomArgs = bloomParser.parse_args()

try: 
    if (bloomArgs.path):
        listdir(bloomArgs.path)

    if (bloomArgs.localPath):
        bloomFilterClient = setHome(bloomArgs.localPath, bloomFilterClient, bloomArgs.verbose)
        print(bloomFilterClient.globalBloomFilter)

    if (bloomArgs.extPath):
        setExt(bloomArgs.extPath)

    if (bloomArgs.sync):
        if not check():
            exit(0)
        moveLocaltoExt()

except argparse.ArgumentError as e:
    print(e)

    