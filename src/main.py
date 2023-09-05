from pathlib import Path
import argparse
import json

bloomParser = argparse.ArgumentParser()
bloomParser.add_argument("path")

bloomArgs = bloomParser.parse_args()

bloomTarget = Path(bloomArgs.path)
 
bloomDirs = json.loads(open("dirs.json", "r").read())

homeDir = bloomDirs["home"]
extDir = bloomDirs["external"]

print(homeDir, extDir)

if not bloomTarget.exists():
    print("Directory does not exist!")
    exit(1)

if not (homeDir and extDir):
    print("Home/external dirs not set, use flags --home or --ext to set respective dirs.")
    exit(2)

for entry, file in enumerate(bloomTarget.iterdir()):
    print(str(file).removeprefix(str(bloomTarget)))
    if entry > 10:
        print("...continued")
        exit(0)
