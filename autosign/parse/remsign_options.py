#!/usr/bin/env python2

##
# autosign
# https://github.com/leosartaj/autosign.git
# 
# copyright (c) 2014 sartaj singh
# licensed under the mit license.
##

"""
Contains helper functions for parsing arguments
"""

import argparse # parsing the options
import parent_parser

def parse_args():
    """
    Parses the arguments
    """
    parent = parent_parser.gen_parent_parser()
    parser = argparse.ArgumentParser(parents=[parent], description='Remove signs from signed python files easily')

    rsign_group = parser.add_argument_group('rsign')

    help = "The target for sign removal."
    rsign_group.add_argument('target', type=str, help=help)

    args = parser.parse_args()

    return args

