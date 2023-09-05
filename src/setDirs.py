import json

def setHome(path):
    bloomFile = open("../dirs.json", "r+").read()
    inObj = json.load(bloomFile)
    extDir = inObj["external"]

    bloomObj = {
        "home": path,
        "external": extDir
    }

    bloomFile.write(json.dump(bloomObj))
    print("Local path", path, "added")


def setExt(path):
    bloomFile = open("../dirs.json", "r+")
    inObj = json.load(bloomFile)
    homeDir = inObj["home"]

    bloomObj = {
        "home": homeDir,
        "external": path
    }

    bloomFile.write(json.dump(bloomObj))
    print("External path", path, "added")