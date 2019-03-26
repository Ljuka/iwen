from XD import XD
import Parser
import ColorMaker
import shutil
import os
import webbrowser
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

importFilePath = ''

def openFileForImport(self):
    global importFilePath
    importFilePath = fd.askopenfilename()
    if importFilePath is not '':
        splitted = importFilePath.split('.')
        if splitted[-1] == 'xd':
            importBttn.config(highlightbackground="#137c23", text="File uploaded")
        else:
            importFilePath = ''
            importBttn.config(highlightbackground="#3e4149", text="Wrong format. Choose .xd file")

def openFileForExport(self):
    global importFilePath
    exportPath = fd.askdirectory()
    if exportPath is not '':
        if importFilePath is not '':
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
                            if os.name == "posix":
                                ColorMaker.makeJsonFile(exportPath, colours)

                                clr = ColorMaker.makeClrFile(exportPath)
                                if clr != "OK" and clr != "X":
                                    messagebox.showerror("Error", clr)
                                    ColorMaker.removeUnzippedDir(exportPath)
                                    exit()

                            ColorMaker.makeColourCodeForAndroid(exportPath, colours)
                            shutil.make_archive(exportPath + '/Iwen Colours', 'zip', exportPath + '/Iwen Colours')
                            ColorMaker.removeUnzippedDir(exportPath)
                            messagebox.showinfo("Success", "Colors generated successfully!")
                            exportPath = os.path.realpath(exportPath)
                            # Open folder - try for windows, else go for mac
                            try:
                                os.startfile(exportPath)
                            except:
                                os.system(f'open {os.path.realpath(exportPath)}')
                    #         Reset buttons
                            importFilePath = ''
                            exportPath = ''
                            importBttn.config(highlightbackground="#3e4149", text="Choose XD file")

                    except IndexError:
                        print("Error")
        else:
            messagebox.showerror("Error", "Choose XD file first!")


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
root.geometry("%dx%d+{}+{}".format(positionRight, positionDown) %(280, 160))

importBttn = Button(root, text="Choose XD file", highlightbackground='#3e4149')
importBttn.place(relx=.5, rely=.25, anchor="center")
importBttn.config(height=3, width=22)
importBttn.bind("<Button-1>", openFileForImport)

exportBttn = Button(root, text="Generate colours", highlightbackground='#4436af') #137c23
exportBttn.place(relx=.5, rely=.7, anchor="center")
exportBttn.config(height=3, width=22)
exportBttn.bind("<Button-1>", openFileForExport)



root.mainloop()
