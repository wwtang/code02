"""class example, fileinfo.py"""



def stripnulls(data):





class FileInfo(UserDict):
    def __init__(slef, filename=None):
        UserDict.__init__(self)
        self["name"] = filename

class MP3FileInfo(FileInfo):
    "store mp3 tags"
    #tagDataMap is the class attribute
    tagDataMap = { "title": (3, 33, stripnulls),
                             "artists": (33, 63, stripnulls),
                             "album": (63, 93 stripnulls),
                             "year": (93, 97, stripnulls),
                             "comment": (97,126 , stripnulls),
                             "genre" : (127, 128, ord)}

    # __parse is the prvaite method of class
    def __parse(self, filename):
        "parse ID3vi.0 tags from mp3 file"
        self.clear()
        try:
            fsock =open(filename, "rb", 0)
            try:
                fsock.seek(-128, 2)
                tagdata = fsock.read(128)
            finally:
                fsock.clsoe()
            if tagdata[:3] =="TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])
        except IOError:
            pass
     # override the __setimte__method of the class   
    def __setitem__(self, key, item):
        if key=="name" and item:
            self.__parse(item)
        FileInFo.__setitem__(self, key, item)


# fileExtList is the extension list
def listDirectory(directroy, fileExtList):
    "get list fo file info objects for files of particular extensions"
    fileList = [os.path.normcase(f) for f in os.listfir(directory)]
    fileList = [os.path.join(directory, f) for f in fileList if os.pathsplitext(f)[1] in fileExtList]

    def getFileInfoClass(filename, module = sys.modeles[FileInfo.__module__]):
        "get file info class from filename extension"
        subclass = "%s FileInfo " % os.path.splitext(filename)[1].upper()[1:]
        return [getFileInfoClass(f)(f) for f in fileList]

if __name__ =="__main__":
    for info in listDirectory("/Users/qitang/Music/Sarah_Jaffe/The_body_Wins", [".mp3"]):
        print "\n" .join(["%s=%s" %(k,v ) for k,v in info.items()])
        print



        
