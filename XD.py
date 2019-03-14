from zipfile import ZipFile

class XD:

    def __init__(self, path):
        self._name = None
        self._path = path
        self._thumbnail_path = None
        self._preview_path = None
        self._color_swatches = None
        self._gradients = None
        self._artboards = None
        self._file = ZipFile(path, 'r')
