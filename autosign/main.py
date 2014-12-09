#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

import os
import re
import constants
import exceptions

"""
Main functions
"""

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

def checkRe(exp, line):
    """
    Checks a line if it follows a regular expression or not
    """
    result = exp.match(line)
    if result:
        return True
    return False

def hasInter(fName):
    """
    Checks if a file starts with a #! 
    directing to use python interpreter
    """ 
    exp = re.compile('^#!.*python.*$')
    with open(fName, 'r') as handler:
        lines = handler.readlines()
        if len(lines) and checkRe(exp, lines[0]):
            return True
    return False

def removeInter(fName):
    """
    Checks if a file starts with a #! 
    directing to use python interpreter
    if it has removes and returns the line
    else returns None
    """
    inter = None
    if not hasInter(fName):
        return inter
    with open(fName, 'r') as handler:
        lines = handler.readlines()
    exp = re.compile('^#!.*python.*$')
    with open(fName, 'w') as handler:
        for line in lines:
            if not checkRe(exp, line):
                handler.write(line)
            else:
                inter = line
    return inter

def isPy(fName):
    """
    checks if file is python or not
    checks if file has .py extension
    or checks if first line contains #!
    and directs the use of python interpreter
    """
    name, ext = os.path.splitext(fName)
    if ext == '.py' or hasInter(fName):
        return True

    return False

def checkTemplate(fName):
    """
    checks if the file
    is a proper template or not
    file should only contain a single signature
    before the signature line startin with #! is allowed
    extra lines are allowed before or after signature
    """
    start, end = getIndex(fName)
    if start == None or end == None:
        return False
    handler = open(fName, 'r')
    lines = handler.readlines()
    add = 0
    for index, line in enumerate(lines):
        if line[:2] == constants.__inter__ and index < start:
            add += 1
        elif line == os.linesep and (index < start or index > end):
            add += 1
    if len(lines) - 1 == end - start + add:
        return True
    return False

def sign(signFile, fName, force=False):
    """
    Signs an unsigned file by default
    if force is True also replaces sign of signed files
    """
    if not checkTemplate(signFile):
        raise exceptions.TemplateError('Incorrect Template')

    with open(signFile, 'r') as sign: # sign to be added
        sign_lines = sign.readlines()
        temp_len = len(sign_lines)

    if not isSign(fName):
        inter_f = removeInter(fName)
        with open(fName, 'r') as handler:
            lines = handler.readlines()
        with open(fName, 'w') as handler:
            if inter_f != None and not hasInter(signFile):
                handler.write(inter_f)
            for line in sign_lines:
                handler.write(line)
            for line in lines:
                handler.write(line)
    elif force:
        inter_f = removeInter(fName)
        start, end = getIndex(fName)
        with open(fName, 'r') as handler:
            lines = handler.readlines()
        with open(fName, 'w') as handler:
            if inter_f != None and not hasInter(signFile):
                handler.write(inter_f)
            for line in sign_lines:
                handler.write(line)
            for index, line in enumerate(lines):
                if index > end:
                    handler.write(line)

def signFiles(signfile, fName, recursive=False, force=False):
    """
    recursive implementation of main.sign
    signs a file
    signs all the files in a directory
    """
    if os.path.isfile(fName) and isPy(fName):
        sign(signfile, fName, force)
    elif os.path.isdir(fName):
        for filename in os.listdir(fName):
            path = os.path.join(fName, filename)
            if os.path.isdir(path) and recursive:
                signFiles(signfile, path, recursive, force)
            elif os.path.isfile(path) and isPy(path):
                sign(signfile, path, force)

def removeSign(fName):
    """
    Removes sign from a signed file
    does not remove shebang line
    does not remove extra lines that were added 
    after/before the signature when the file was signed
    raises UnsignedError if file not signed
    """
    if not isSign(fName):
        raise exceptions.UnsignedError("File not signed")

    with open(fName, 'r') as handler:
        lines = handler.readlines()

    start, end = getIndex(fName)
    with open(fName, 'w') as handler:
        for index in range(len(lines)):
            if index < start or index > end:
                handler.write(lines[index])

def removeSignFiles(fName, recursive=False):
    """
    recursive implementation of main.removeSign
    removes sign from a python file 
    removes signs from all the python files in a directory
    """
    if os.path.isfile(fName) and isSign(fName) and isPy(fName):
        removeSign(fName)
    elif os.path.isdir(fName):
        for filename in os.listdir(fName):
            path = os.path.join(fName, filename)
            if os.path.isdir(path) and recursive:
                removeSignFiles(path, recursive)
            elif os.path.isfile(path) and isSign(path) and isPy(path):
                removeSign(path)
