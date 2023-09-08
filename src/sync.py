from bloomfilter import BloomFilter
from pathlib import Path
import json
import os
import shutil
from datetime import datetime

class BloomSync:
    def __init__(self) -> None:
        with open("../dirs.json", "r") as bloomDir:
            inObj = json.loads(bloomDir.read())
            self.extDirStr: str = inObj["external"]
            self.localDirStr: str = inObj["home"]
            self.extDir = Path(self.extDirStr)
            self.localDir = Path(self.localDirStr)

    def moveExtToLocal(self, filter: BloomFilter, verbose: bool) -> BloomFilter:
        with open("../logs.txt", "w+") as log:
            for file in self.localDir.iterdir():
                filter.getSum(str(file).removeprefix(self.localDirStr + '/'))
                filter.insertBloomFilter()
                if verbose:
                    print(f"Hashed {str(file)}")
            
            copied = unchanged = 0
            for file in self.extDir.iterdir():
                rawFileName = str(file).removeprefix(self.extDirStr + '/')
                confident = filter.searchBloomFilter(rawFileName)
                timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

                if confident and Path(self.localDirStr + '/' + rawFileName).exists():

                    if verbose:
                        print(f"[{timestamp}] {file} exists.")
                    
                    log.write(f"[{timestamp}] {self.localDirStr + '/' + rawFileName} exists.\n")
                    unchanged += 1
                    
                else:
                    if verbose:
                        print(f"[{timestamp}] {self.localDirStr + '/' + rawFileName} does not exist, syncing.")
            
                    log.write(f"[{timestamp}] {self.localDirStr + '/' + rawFileName} does not exist, syncing.\n")
                    shutil.copy(str(file), self.localDirStr + '/' + rawFileName)
                    copied += 1

            if verbose:
                print(f"{copied} files copied, {unchanged} files unchanged.") 
            log.write(f"{copied} files copied, {unchanged} files unchanged.\n")

        return filter
    
    def moveLocalToExt(self, filter: BloomFilter, verbose: bool) -> BloomFilter:
        with open("../logs.txt", "r+") as log:
            log.seek(0, 2)
            log.write("Starting job")
            for file in self.extDir.iterdir():
                filter.getSum(str(file).removeprefix(self.extDirStr + '/'))
                filter.insertBloomFilter()
                if verbose:
                    print(f"Hashed {str(file)}")
            
            copied = unchanged = 0
            for file in self.localDir.iterdir():
                rawFileName = str(file).removeprefix(self.localDirStr + '/')
                confident = filter.searchBloomFilter(rawFileName)
                timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

                if confident and Path(self.extDirStr + '/' + rawFileName).exists():

                    if verbose:
                        print(f"[{timestamp}] {file} exists.")
                    
                    log.write(f"[{timestamp}] {self.extDirStr + '/' + rawFileName} exists.\n")
                    unchanged += 1
                    
                else:
                    if verbose:
                        print(f"[{timestamp}] {self.extDirStr + '/' + rawFileName} does not exist, syncing.")
            
                    log.write(f"[{timestamp}] {self.extDirStr + '/' + rawFileName} does not exist, syncing.\n")
                    shutil.copy(str(file), self.extDirStr + '/' + rawFileName)
                    copied += 1

            if verbose:
                print(f"{copied} files copied, {unchanged} files unchanged.") 
            log.write(f"{copied} files copied, {unchanged} files unchanged.\n")

        return filter