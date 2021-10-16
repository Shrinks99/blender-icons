#!/usr/bin/python
# Requires Python >= 3
"""
Filename:
    optimize.py

Function:
    This script calls SVGO and makes sure that SVGO is executed correctly on all platforms

Important notes:
    Code should be formatted by black and checked for bugs by pylint
"""
from sys import platform
import os

# We'll use NPX to run SVGO which optimizes the files
MAIN_COMMAND = "npx svgo -f blender-icons -o blender-icons"

# These two commands are used on Unix-based OSes and Windows
# respectively to check if the `npx` command exists
UNIX_COMMAND = "command -v npx &> /dev/null"
WINDOWS_COMMAND = "WHERE scp >nul 2>nul"

# These variables store the error warning if NPX is not found
ERROR_WARNING = "ERROR: You don't have NPX installed or it's not installed correctly!"
HELP_LINK = "https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"
ERROR_INSTRUCTION = "To troubleshoot this issue, visit " + HELP_LINK

# This variable prints the success message
SUCCESS_MESSAGE = "Great! SVGO will begin optimizing the SVGs shortly...\n"

# Linux & macOS (basically any Unix-based OS)
if platform in ("linux", "linux2", "darwin"):
    # If exit code is 0 that means NPX is found
    if os.system(UNIX_COMMAND) == 0:
        print(SUCCESS_MESSAGE)
        os.system(MAIN_COMMAND)
    else:
        print(ERROR_WARNING)
        print(ERROR_INSTRUCTION)
# Windows
elif platform == "win32":
    # If exit code is 0 that means NPX is found
    if os.system(WINDOWS_COMMAND) == 0:
        print(SUCCESS_MESSAGE)
        os.system(MAIN_COMMAND)
    else:
        print(ERROR_WARNING)
        print(ERROR_INSTRUCTION)
