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
    parser = argparse.ArgumentParser(parents=[parent], description='Statistics utility of autosign')

    exclusive = parser.add_mutually_exclusive_group()

    help = "The target on which data should be collected"
    parser.add_argument('target', type=str, help=help)

    help = "For Verbose Output."
    parser.add_argument('--verbose',  action='store_true', help=help, dest='verbose')

    help = "Complete Statistics"
    exclusive.add_argument('--complete', '-c',  action='store_true', help=help, dest='complete')

    help = "Count The signed files"
    exclusive.add_argument('--sign', '-s',  action='store_true', help=help, dest='sign')

    help = "Count The unsigned files"
    exclusive.add_argument('--usign', '-u',  action='store_true', help=help, dest='usign')

    args = parser.parse_args()

    return args
