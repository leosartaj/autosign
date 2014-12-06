import os
import constants

def getPath(dire, fName):
    """
    Joins and returns the path
    """
    path = os.path.join(dire, fName)
    return path

def getIndex(dire, fName):
    """
    returns the start and end of a signature in a file
    returns None if __sigstart__ or __sigend__ not found
    """
    path = getPath(dire, fName)
    handler = open(path)

    start, end = None, None
    for index, line in enumerate(handler):
        if line[:2] == constants.__sigstart__ and start == None:
            start = index
        elif line[:2] == constants.__sigend__ and end == None:
            end = index
            break
        elif line[0] != constants.__sigline__ and start != None:
            start, end = None, None
            break
    if start != None and end != None:
        return start, end
    return None, None

def isSign(dire, fName):
    """
    Checks if a file is already signed
    """
    start, end = getIndex(dire, fName)
    if start != None and end != None:
        return True
    return False

if __name__ == '__main__':
    pass
