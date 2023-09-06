import json
from bloomfilter import BloomFilter
from pathlib import Path
from check import check

def setHome(path, filter: BloomFilter, verbose: bool) -> BloomFilter:
    with open("../dirs.json", "r+") as bloomDir:
        try:
            inObj = json.loads(bloomDir.read())
            extDir = inObj["external"]
            if path == extDir and extDir != "":
                raise Exception("Local and external directories cannot be the same.")

            if not Path(path).exists():
                raise Exception("Directory is invalid or does not exist.")
            
            bloomObj = {
                "home": path,
                "external": extDir
            }
            bloomDir.seek(0)
            bloomDir.write(json.dumps(bloomObj, indent=4))
            print("Local path", path, "added.")

            targetPath = Path(path)
            for file in targetPath.iterdir(): 
                filter.getSum(str(file))
                filter.insertBloomFilter()
                if verbose:
                    print(f"Hashed {str(file)}")
            
            return filter
        
        except FileNotFoundError:
            raise Exception("Config JSON not found.")
    
def setExt(path):
    try:    
        with open("../dirs.json", "r+") as bloomDir:
            inObj = json.loads(bloomDir.read())
            homeDir = inObj["home"]
            if path == homeDir and homeDir != "":
                raise Exception("Local and external directories cannot be the same.")

            if not Path(path).exists():
                raise Exception("Directory is invalid or does not exist.")
            
            bloomObj = {
                "home": homeDir,
                "external": path
            }
            bloomDir.seek(0)
            bloomDir.write(json.dumps(bloomObj, indent=4))
            print("External path", path, "added.")

    except FileNotFoundError:
        raise Exception("Config JSON not found.")
    