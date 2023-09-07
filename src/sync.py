from bloomfilter import BloomFilter
from pathlib import Path
import json
import os
import shutil
from datetime import datetime


def moveLocaltoExt(filter: BloomFilter, verbose: bool) -> BloomFilter:
    with open("../dirs.json", "r") as bloomDir:
        inObj = json.loads(bloomDir.read())
        extDirStr: str = inObj["external"]
        localDirStr: str = inObj["home"]
        extDir = Path(extDirStr)
        localDir = Path(localDirStr)
    
    with open("../logs.txt", "w+") as log:
        for file in localDir.iterdir():
            filter.getSum(str(file).removeprefix(localDirStr + '/'))
            filter.insertBloomFilter()
            if verbose:
                print(f"Hashed {str(file)}")
        
        copied = unchanged = 0
        for file in extDir.iterdir():
            confident = filter.searchBloomFilter(str(file).removeprefix(extDirStr + '/'))
            if confident and Path(localDirStr + '/' + str(file).removeprefix(extDirStr + '/')).exists():
                if verbose:
                    print(f"[{datetime.now()}] {file} exists.")
                
                log.write(f"[{datetime.now()}] {localDirStr + '/' + str(file).removeprefix(extDirStr + '/')} exists.\n")
                unchanged += 1
                
            else:
                if verbose:
                    print(f"[{datetime.now()}] {localDirStr + '/' + str(file).removeprefix(extDirStr + '/')} does not exist, syncing.")
        
                log.write(f"[{datetime.now()}] {localDirStr + '/' + str(file).removeprefix(extDirStr + '/')} does not exist, syncing.\n")
                shutil.copy(str(file), localDirStr + '/' + str(file).removeprefix(extDirStr + '/'))
                copied += 1

        if verbose:
            print(f"{copied} files copied, {unchanged} files unchanged.") 
        log.write(f"{copied} files copied, {unchanged} files unchanged.\n")        
    return filter