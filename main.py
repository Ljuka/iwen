from XD import XD
import Parser
import ColorMaker
import shutil
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

importFilePath = ''

def openFileForImport(self):
    global importFilePath
    importBttn.config(highlightbackground="#137c23")
    importFilePath = fd.askopenfilename()

def openFileForExport(self):
    global importFilePath
    exportPath = fd.askdirectory()
    if exportPath is not '':
        zipFile = XD(importFilePath)
        ColorMaker.createStartFolderStructure(exportPath)

        with zipFile._file as xd:
            for file in xd.filelist:
                try:
                    orig_filename = file.orig_filename
                    if orig_filename in 'resources/graphics/graphicContent.agc':
                        parsedColourFile = Parser.parseColourFile(orig_filename, xd)
                        colours = parsedColourFile['resources']['meta']['ux']['documentLibrary']['elements']
                        ColorMaker.makeColourCodeForIOS(exportPath, colours)
                        ColorMaker.makeColourPaletteXcassets(exportPath, colours)
                        ColorMaker.makeColourCodeForAndroid(exportPath, colours)
                        shutil.make_archive(exportPath + '/Iwen Colours', 'zip', exportPath + '/Iwen Colours')
                        ColorMaker.removeUnzippedDir(exportPath)
                        messagebox.showinfo("Success", "Colors generated successfully!")
                except IndexError:
                    print("Error")


root = Tk()
root.resizable(0, 0)
root.winfo_toplevel().title("Iwen")

# Pozadina
root.config(bg="white")

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
root.geometry("%dx%d+{}+{}".format(positionRight, positionDown) %(250, 160))

importBttn = Button(root, text="Choose XD file", highlightbackground='#3e4149')
importBttn.place(relx=.5, rely=.25, anchor="center")
importBttn.config(height=3, width=20)
importBttn.bind("<Button-1>", openFileForImport)

exportBttn = Button(root, text="Generate colours", highlightbackground='#4436af') #137c23
exportBttn.place(relx=.5, rely=.7, anchor="center")
exportBttn.config(height=3, width=20)
exportBttn.bind("<Button-1>", openFileForExport)




root.mainloop()
