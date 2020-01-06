class PathMannanger:

    def __init__(self,localPath,baseApiPath):
        self.localPath = localPath
        self.baseApiPath = baseApiPath

    def getApiModulePath(self,apiModuleName):
        return self.localPath+'Courses/'+apiModuleName+'/'+self.baseApiPath

def makeAplicationLibrariesAvaliable() :
    import sys
    from pathlib import Path

    localPath = str(Path.home()) + '/'
    baseApiPath = 'api/src/'
    pathMannanger = PathMannanger(localPath,baseApiPath)

    sys.path.append(pathMannanger.localPath+'Morgs/')
    sys.path.append(pathMannanger.localPath+'Courses/course/'+pathMannanger.baseApiPath)
    sys.path.append(pathMannanger.localPath+'Courses/desktop/'+pathMannanger.baseApiPath)
    sys.path.append(pathMannanger.localPath+'Courses/editor/'+pathMannanger.baseApiPath)

    return pathMannanger
