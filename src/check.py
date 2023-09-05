from pathlib import Path
import json

def check():
    bloomDirs = json.loads(open("../dirs.json", "r").read())

    homeDir = bloomDirs["home"]
    extDir = bloomDirs["external"]

    if not (homeDir and extDir):
        print("[WARNING] Home/external dirs not set, use flags --home or --ext to set respective dirs.")