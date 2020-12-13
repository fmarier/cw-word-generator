#!/usr/bin/env python3
# -*- mode: python -*-
"""
CW Word Generator - generate words for CW reading practice.

Copyright (C) 2020  Francois Marier <va7gpl@fmarier.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import random
import sys


def characters(stages, extra_chars):
    chars = extra_chars

    # Add characters from each stage of ynotsailing.com course.
    if '1' in stages:
        chars += 'taeons8'
    if '2' in stages:
        chars += 'irh0dl2u'
    if '3' in stages:
        chars += 'cwf9my1'
    if '4' in stages:
        chars += 'gbvp37'
    if '5' in stages:
        chars += 'kjx4/5'
    if '6' in stages:
        chars += 'z56,q'

    return chars


def generate_word(chars, length):
    word = ""
    for dummy in range(length):
        word += chars[random.randrange(len(chars))]  # nosec
    return word


def main():
    parser = argparse.ArgumentParser(description="CW word generator")
    parser.add_argument('characters', type=str, nargs='?',
                        default='', help='all allowed characters')
    parser.add_argument('-l', '--length', dest='length',
                        type=int, default=5,
                        help='length of each word')
    parser.add_argument('-n', '--number', dest='number',
                        type=int, default=1,
                        help='number of words to generate')
    parser.add_argument('-s', '--stages', dest='stages',
                        type=str, default='',
                        help='YnotSailing stages to include')
    args = parser.parse_args()

    extra_chars = args.characters
    if not extra_chars and not args.stages:
        # Default to all characters on the Canadian exam.
        extra_chars = 'abcdefghijklmnopqrstuvwxyz1234567890.,?/@'

    random.seed()
    for dummy in range(args.number):
        print(generate_word(characters(args.stages, extra_chars), args.length))
    return 0


sys.exit(main())
