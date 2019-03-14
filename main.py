from XD import XD
import Parser
import ColorMaker
import shutil
# import tkinter

xdPath = input("Please enter XD file: ")
zipFile = XD(xdPath)
ColorMaker.createStartFolderStructure('/Users/ljuka/Desktop')

with zipFile._file as xd:
    for file in xd.filelist:
        try:
            orig_filename = file.orig_filename
            if orig_filename in 'resources/graphics/graphicContent.agc':
                parsedColourFile = Parser.parseColourFile(orig_filename, xd)
                colours = parsedColourFile['resources']['meta']['ux']['documentLibrary']['elements']
                ColorMaker.makeColourCodeForIOS('/Users/ljuka/Desktop', colours)
                ColorMaker.makeColourPaletteXcassets('/Users/ljuka/Desktop', colours)
                ColorMaker.makeColourCodeForAndroid('/Users/ljuka/Desktop', colours)
                shutil.make_archive('/Users/ljuka/Desktop/Iwen Colours', 'zip', '/Users/ljuka/Desktop/Iwen Colours')
                ColorMaker.removeUnzippedDir('/Users/ljuka/Desktop')
        except IndexError:
            print("Error")
