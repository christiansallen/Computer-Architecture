#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

if len(sys.argv) != 2:
    print("usage: ls8.py filename")
    sys.exit(1)
progname = sys.argv[1]
address = 0


cpu.load(progname)
cpu.run()
