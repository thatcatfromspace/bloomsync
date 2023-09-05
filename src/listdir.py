from pathlib import Path

def listdir(path):
    bloomTarget = Path(path)
    if not bloomTarget.exists():
        print("Directory does not exist!")
        exit(1)

    for entry, file in enumerate(bloomTarget.iterdir()):
        if len(list(bloomTarget.iterdir())) < 2:
            print(str(file).removeprefix(str(bloomTarget) + '/'))
            exit(0)
        elif entry < len(list(bloomTarget.iterdir()))/2:
            print(str(file).removeprefix(str(bloomTarget) + '/'))
        else:
            print(f"... around", int(len(list(bloomTarget.iterdir()))/2), "more")
            exit(0)
