import argparse
from listdir import listdir
from check import check
from setDirs import setHome, setExt


bloomParser = argparse.ArgumentParser(description="Sync contents of two independent directories.")
bloomParser.add_argument("-ls", "--listdir", type=listdir, help="list the contents of a directory")
bloomParser.add_argument("-l", "--local", type=setHome, help="sets home directory")
bloomParser.add_argument("-e", "--external", type=setExt, help="sets external directory")

bloomArgs = bloomParser.parse_args()

if (bloomArgs.ls):
    check()
    listdir(bloomArgs.ls)

if (bloomArgs.l):
    check()
    setHome(bloomArgs.l)

if (bloomArgs.e):
    check()
    setExt(bloomArgs.e)
