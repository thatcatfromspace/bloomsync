import json
import logging
import warnings


def check() -> None:
    bloomDirs = json.loads(open("/home/.bloomsync/dirs.json", "r").read())

    homeDir = bloomDirs["home"]
    extDir = bloomDirs["external"]

    if not (homeDir and extDir):
        logging.error("[WARNING] Home/external directories not set, use flags -h or -e to set respective dirs.")
        raise warnings.warn("[WARNING] Home/external directories not set, use flags -h or -e to set respective dirs.", Warning)
