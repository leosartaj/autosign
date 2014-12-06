import os
import constants
import exceptions

def getIndex(fName):
    """
    returns the start and end of a signature in a file
    returns None if __sigstart__ or __sigend__ not found
    """
    handler = open(fName)

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

def isSign(fName):
    """
    Checks if a file is already signed
    """
    start, end = getIndex(fName)
    if start != None and end != None:
        return True
    return False

def checkTemplate(fName):
    """
    checks if the file
    is a proper template or not
    file should only contain a single signature
    no extra lines are allowed
    """
    start, end = getIndex(fName)
    if start == None or end == None:
        return False
    handler = open(fName)
    lines = handler.read().split('\n')
    if len(lines) - 2 == (end - start):
        return True
    return False

def sign(signFile, fName, force=False):
    """
    Signs an unsigned file by default
    if force is True also replaces sign of signed files
    """
    if not checkTemplate(signFile):
        raise exceptions.TemplateError('Incorrect Template')

    sign = open(signFile) # sign to be added
    handler = open(fName, 'a')

    if not isSign(fName):
        handler.seek(0, 0)
        lines = sign.read()
        handler.write(lines)
