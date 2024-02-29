from bloomfilter import BloomFilter
from datetime import datetime
import json
import logging
from pathlib import Path
import shutil

class BloomSync:
    def __init__(self) -> None:
        with open("/home/.bloomsync/dirs.json", "r") as bloomDir:
            inObj = json.loads(bloomDir.read())
            self.extDirStr: str = inObj["external"]
            self.localDirStr: str = inObj["home"]
            self.extDir = Path(self.extDirStr)
            self.localDir = Path(self.localDirStr)

    def moveExtToLocal(self, filter: BloomFilter, verbose: bool) -> BloomFilter:
        try:
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
                    
                    logging.info(f"[{timestamp}] {self.localDirStr + '/' + rawFileName} exists.\n")
                    unchanged += 1
                    
                else:
                    if verbose:
                        print(f"[{timestamp}] {self.localDirStr + '/' + rawFileName} does not exist, syncing.")
            
                    logging.info(f"[{timestamp}] {self.localDirStr + '/' + rawFileName} does not exist, syncing.\n")
                    shutil.copy(str(file), self.localDirStr + '/' + rawFileName)
                    copied += 1

            if verbose:
                logging.info(f"{copied} files copied, {unchanged} files unchanged.") 

            return filter

        except:
            logging.error()

        
    def moveLocalToExt(self, filter: BloomFilter, verbose: bool) -> BloomFilter:
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
                
                logging.info(f"[{timestamp}] {self.extDirStr + '/' + rawFileName} exists.\n")
                unchanged += 1
                
            else:
                if verbose:
                    print(f"[{timestamp}] {self.extDirStr + '/' + rawFileName} does not exist, syncing.")
        
                logging.info(f"[{timestamp}] {self.extDirStr + '/' + rawFileName} does not exist, syncing.\n")
                shutil.copy(str(file), self.extDirStr + '/' + rawFileName)
                copied += 1

        if verbose:
            print(f"{copied} files copied, {unchanged} files unchanged.") 
        logging.info(f"{copied} files copied, {unchanged} files unchanged.\n")

        return filter