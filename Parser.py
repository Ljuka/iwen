import json

def parseColourFile(path, file):
    colourFile = file.read(path)
    colourData = json.loads(colourFile.decode('utf-8'))
    return colourData