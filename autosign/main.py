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
import exce

"""
Main functions
"""

def getIndex(fName, options):
    """
    returns the start and end of a signature in a file
    returns None if no signature found
    """
    handler = open(fName)

    opt_start, opt_end, opt_line = options.start, options.end, options.line
    ls, le, ll = len(opt_start), len(opt_end), len(opt_line)

    start, end = None, None
    for index, line in enumerate(handler):
        if line[:ls] == opt_start and start == None:
            start = index
        elif line[:le] == opt_end and end == None:
            end = index
            break
        elif line[:ll] != opt_line and start != None:
            start, end = None, None
            break
    if start != None and end != None:
        return start, end
    return None, None

def isSign(fName, options):
    """
    Checks if a file is already signed
    """
    start, end = getIndex(fName, options)
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

def hasInter(fName, allow=None):
    """
    Checks if a file has a special line
    matching allow
    """ 
    if not allow:
        return False
    exp = re.compile(allow)
    with open(fName, 'r') as handler:
        lines = handler.readlines()
        if len(lines) and checkRe(exp, lines[0]):
            return True
    return False

def removeInter(fName, allow=None):
    """
    Checks if a file has a line with the passed re
    if it has removes and returns the first matched line
    else returns None
    """
    inter = None
    if not allow:
        return inter
    if not hasInter(fName, allow):
        return inter
    with open(fName, 'r') as handler:
        lines = handler.readlines()
    exp = re.compile(allow)
    with open(fName, 'w') as handler:
        for line in lines:
            if not checkRe(exp, line):
                handler.write(line)
            else:
                inter = line
    return inter

def checkType(fName, ext='.py'):
    """
    checks if file is of a given type
    checks if file has ext extension
    """
    name, extension = os.path.splitext(fName)
    if extension == ext:
        return True
    return False

def checkTemplate(fName, options):
    """
    checks if the file
    is a proper template or not
    file should only contain a single signature
    if allow option is set, allows allowed line
    extra lines are allowed before or after signature
    """
    start, end = getIndex(fName, options)
    if start == None or end == None:
        return False

    exp = None
    if options.allow:
        exp = re.compile(options.allow)

    handler = open(fName, 'r')
    lines = handler.readlines()
    add = 0
    for index, line in enumerate(lines):
        if exp and checkRe(exp, line) and index < start:
            add += 1
        elif options.blank and line == os.linesep and (index < start or index > end):
            add += 1
    if len(lines) - 1 == end - start + add:
        return True
    return False

def checkFiles(fName, options, recursive=False):
    """
    yields whether a file is signed or not
    """
    ext = options.ext
    if os.path.isfile(fName) and checkType(fName, ext):
        yield fName, isSign(fName, options)
    elif os.path.isdir(fName):
        for filename in os.listdir(fName):
            path = os.path.join(fName, filename)
            if os.path.isdir(path) and recursive:
                for filename, val in checkFiles(path, options, recursive):
                    yield filename, val
            elif os.path.isfile(path) and checkType(path, ext):
                yield path, isSign(path, options)

def sign(signFile, fName, options, force=False):
    """
    Signs an unsigned file by default
    if force is True also replaces sign of signed files
    """
    if not checkTemplate(signFile, options):
        raise exce.TemplateError('Incorrect Template')

    with open(signFile, 'r') as sign: # sign to be added
        sign_lines = sign.readlines()
        temp_len = len(sign_lines)

    allow = options.allow
    if not isSign(fName, options):
        inter_f = removeInter(fName, allow)
        with open(fName, 'r') as handler:
            lines = handler.readlines()
        with open(fName, 'w') as handler:
            if inter_f != None and not hasInter(signFile, allow):
                handler.write(inter_f)
            for line in sign_lines:
                handler.write(line)
            for line in lines:
                handler.write(line)
        return True
    elif force:
        inter_f = removeInter(fName, allow)
        start, end = getIndex(fName, options)
        with open(fName, 'r') as handler:
            lines = handler.readlines()
        with open(fName, 'w') as handler:
            if inter_f != None and not hasInter(signFile, allow):
                handler.write(inter_f)
            for line in sign_lines:
                handler.write(line)
            for index, line in enumerate(lines):
                if index > end:
                    handler.write(line)
        return True
    return False

def signFiles(signfile, fName, options, recursive=False, force=False):
    """
    recursive implementation of main.sign
    signs a file
    signs all the files in a directory
    """
    ext = options.ext
    if os.path.isfile(fName) and checkType(fName, ext):
        result = sign(signfile, fName, options, force)
        yield fName, result
    elif os.path.isdir(fName):
        for filename in os.listdir(fName):
            path = os.path.join(fName, filename)
            if os.path.isdir(path) and recursive:
                for filename, val in signFiles(signfile, path, options, recursive, force):
                    yield filename, val
            elif os.path.isfile(path) and checkType(path, ext):
                result = sign(signfile, path, options, force)
                yield path, result

def removeSign(fName, options):
    """
    Removes sign from a signed file
    does not remove shebang line
    does not remove extra lines that were added 
    after/before the signature when the file was signed
    raises UnsignedError if file not signed
    """
    if not isSign(fName, options):
        raise exce.UnsignedError("File not signed")

    with open(fName, 'r') as handler:
        lines = handler.readlines()

    start, end = getIndex(fName, options)
    with open(fName, 'w') as handler:
        for index in range(len(lines)):
            if index < start or index > end:
                handler.write(lines[index])

def removeSignFiles(fName, options, recursive=False):
    """
    recursive implementation of main.removeSign
    removes sign from a python file 
    removes signs from all the python files in a directory
    """
    ext = options.ext
    if os.path.isfile(fName) and isSign(fName, options) and checkType(fName, ext):
        removeSign(fName, options)
        yield fName
    elif os.path.isdir(fName):
        for filename in os.listdir(fName):
            path = os.path.join(fName, filename)
            if os.path.isdir(path) and recursive:
                for filename in removeSignFiles(path, options, recursive):
                    yield path
            elif os.path.isfile(path) and isSign(path, options) and checkType(path, ext):
                removeSign(path, options)
                yield path
