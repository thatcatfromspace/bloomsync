import argparse
from pathlib import Path
from os import getenv

bloomParser = argparse.ArgumentParser()
bloomParser.add_argument("path")
bloomArgs = bloomParser.parse_args()

target = Path(bloomArgs.path)

if not target.exists():
    print("The target directory does not exist.")
    raise SystemExit(1)

# if getenv("HOME_DIR") == "" or getenv("ROOT_DIR") == "":
#     print("Home or external directory have not been set. Use flag -s --home or -s --ext to set the respective directory.")
#     raise SystemExit(2)

for file in target.iterdir():
    print(str(file).removeprefix(str(target)))