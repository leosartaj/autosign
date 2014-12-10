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
import configOptions as co
from configOptions import __rc__

def save_rc(parser, fName=__rc__):
    """
    saves a parser
    and the given path
    """
    with open(fName, 'w') as handler:
        parser.write(handler)

def gen_basic_rc():
    """
    sets up a parser
    sets up basic sections and options
    returns the parser
    """
    parser = SafeConfigParser(allow_no_value=True)

    sec = 'python'
    parser.add_section(sec)
    default = co.DEFAULT_OPTIONS
    for option in default:
        parser.set(sec, option, default[option])
    special = co.SPECIAL_OPTIONS
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

    default = co.DEFAULT_OPTIONS
    for option in default:
        if not option in options:
            options[option] = default[option]
        elif not options[option]:
            options[option] = default[option]

    return options

def parse_rc(rc=__rc__):
    """
    Parses a rc
    returns a dictionary of dictionary
    with each section as key
    and value being a dictionary of options, value pairs
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
