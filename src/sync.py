from bloomfilter import BloomFilter
from pathlib import Path
import json
import os
import shutil
from datetime import datetime


def moveLocaltoExt(filter: BloomFilter, verbose: bool) -> BloomFilter:
    with open("../dirs.json", "r") as bloomDir:
        inObj = json.loads(bloomDir.read())
        extDir = Path(inObj["external"])
        localDir = Path(inObj["home"])
    
    with open("../logs.txt", "w+") as log:
        for file in localDir.iterdir():
            # print(str(file).removeprefix(str(localDir) + '/'))
            filter.getSum(str(file).removeprefix(str(localDir) + '/'))
            filter.insertBloomFilter()
            if verbose:
                print(f"Hashed {str(file)}")
            
        for file in extDir.iterdir():
            confident = filter.searchBloomFilter(str(file))
            if confident and file.exists():
                log.write(f"[{datetime.now()}] {file} exists, replacing.")
                print(str(extDir) + str(file).removeprefix(str(localDir)))
                os.replace(str(Path(file)), str(extDir) + str(file).removeprefix(str(localDir)))
                
            else:
                log.write(f"[{datetime.now()}] {file} does not exist, syncing.")
                print(str(extDir) + str(file).removeprefix(str(localDir)))
                shutil.move(str(Path(file)), str(extDir) + str(file).removeprefix(str(localDir)))
    
    return filter