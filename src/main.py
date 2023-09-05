import argparse
import tabnanny
from listdir import listdir
from check import check
from setDirs import setHome, setExt

tabnanny.check(all)

check()

bloomParser = argparse.ArgumentParser(description="Sync contents of two independent directories.")
bloomParser.add_argument("-ls", "--listdir", dest="path", help="list the contents of a directory")
bloomParser.add_argument("-l", "--local", dest="localPath", help="sets home directory")
bloomParser.add_argument("-e", "--ext", dest="extPath", help="sets external directory")

bloomArgs = bloomParser.parse_args()

if (bloomArgs.path):
    listdir(bloomArgs.path)

if (bloomArgs.localPath):
    setHome(bloomArgs.localPath)

if (bloomArgs.extPath):
    setExt(bloomArgs.extPath)
