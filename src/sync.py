from bloomfilter import BloomFilter
from pathlib import Path
import json

def moveLocaltoExt(path: str, filter: BloomFilter) -> None:
    with open("/home/dinesh/code/bloomsync/dirs.json", "r+") as bloomDir:
        inObj = json.loads(bloomDir.read())
        extDir = inObj["external"]
        localDir = inObj["home"]
    
    

    