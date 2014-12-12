#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

"""
Helper functions for configuration file
"""

import os
from ConfigParser import SafeConfigParser

__rc__ = '.signrc' # default rc name

# defult options for a section
DEFAULT_OPTIONS = {'ext': '.py', 'start': '##', 'line': '#', 'end': '##', 'blank': 'True'}

SPECIAL_OPTIONS = {'allow': '^#!.*python.*$'}

class optionsClass:
    """
    Special class for storing options
    """
    def __init__(self, options):
        self.ext = options['ext']
        self.start = options['start']
        self.line = options['line']
        self.end = options['end']
        self.blank = options['blank']
        self.allow = options['allow']

def save_rc(parser, fName=__rc__):
    """
    saves a parser
    and the given path
    returns the path
    """
    with open(fName, 'w') as handler:
        parser.write(handler)
    return fName

def gen_basic_rc():
    """
    sets up a parser
    sets up basic sections and options
    returns the parser
    """
    parser = SafeConfigParser(allow_no_value=True)

    sec = 'python'
    parser.add_section(sec)
    default = DEFAULT_OPTIONS
    for option in default:
        parser.set(sec, option, default[option])
    special = SPECIAL_OPTIONS
    for option in special:
        parser.set(sec, option, special[option])

    return parser

def gen_parser(rc=__rc__):
    """
    returns the parser for rc
    """
    parser = SafeConfigParser(allow_no_value=True)
    parser.read(rc)
    return parser

def parse_section(parser, section):
    """
    Parses a section
    returns a dictionary
    having options, value
    as key, value pairs
    """
    options = {}
    for name, value in parser.items(section):
        options[name] = value

    default = DEFAULT_OPTIONS
    for option in default:
        if not option in options:
            options[option] = default[option]
        elif not options[option]:
            options[option] = default[option]
    special = SPECIAL_OPTIONS
    for option in special:
        if not option in options:
            options[option] = None # be explicit
    options = optionsClass(options) # wrap it in an object
    return options

def parse_rc(rc=__rc__):
    """
    Parses a rc
    returns a dictionary of objects
    with each section as key
    and value being a object having options as attributes
    """
    parser = gen_parser(rc)
    sections = {}
    for section in parser.sections():
        result = parse_section(parser, section)
        sections[section] = result
    return sections

def find_rc(rc=__rc__):
    """
    First finds a rc in cwd
    if not found then looks
    in HOME
    if found returns the path
    else returns None
    """
    cwd = os.getcwd()
    for filename in os.listdir(cwd):
        if filename == __rc__:
            path = os.path.join(cwd, filename)
            return path
    home = os.environ['HOME']
    home = os.path.realpath(home)
    for filename in os.listdir(home):
        if filename == __rc__:
            path = os.path.join(home, filename)
            return path
    return None
