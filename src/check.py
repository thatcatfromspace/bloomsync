from pathlib import Path
import json

def check() -> bool:
    bloomDirs = json.loads(open("../dirs.json", "r").read())

    homeDir = bloomDirs["home"]
    extDir = bloomDirs["external"]

    if not (homeDir and extDir):
        print("[WARNING] Home/external directories not set, use flags -h or -e to set respective dirs.")
        return False

    else:
        return True