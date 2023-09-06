import json
import warnings

def check() -> None:
    bloomDirs = json.loads(open("/home/dinesh/code/bloomsync/dirs.json", "r").read())

    homeDir = bloomDirs["home"]
    extDir = bloomDirs["external"]

    if not (homeDir and extDir):
        raise warnings.warn("[WARNING] Home/external directories not set, use flags -h or -e to set respective dirs.", Warning)
