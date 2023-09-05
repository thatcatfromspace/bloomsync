import json

def setHome(path):
    with open("../dirs.json", "r+") as bloomDir:
        inObj = json.loads(bloomDir.read())
        extDir = inObj["external"]
        if path == extDir and extDir != "":
            print("Local and external directories cannot be the same.")
            exit(0)

        bloomObj = {
            "home": path,
            "external": extDir
        }
        bloomDir.seek(0)
        bloomDir.write(json.dumps(bloomObj, indent=4))
        print("Local path", path, "added.")

def setExt(path):
    with open("../dirs.json", "r+") as bloomDir:
        inObj = json.loads(bloomDir.read())
        homeDir = inObj["home"]
        if path == homeDir and homeDir != "":
            print("Local and external directories cannot be the same.")
            exit(0)

        bloomObj = {
            "home": homeDir,
            "external": path
        }
        bloomDir.seek(0)
        bloomDir.write(json.dumps(bloomObj, indent=4))
        print("External path", path, "added.")