#!/usr/bin/python
# Requires Python >= 3
"""
This script calls SVGO and makes sure that SVGO is executed correctly on all platforms
"""
from sys import platform
import os

# We'll use NPX to run SVGO which optimizes the files
MAIN_COMMAND = "npx svgo -f Lcn-NIS8Eh8o -o Lcn-NIS8Eh8o/"

# These two commands are used on Unix-based OSes and Windows
# respectively to check if the `npx` command exists
UNIX_COMMAND = "command -v npx &> /dev/null"
WINDOWS_COMMAND = "WHERE scp >nul 2>nul"

# These variables store the error warning if NPX is not found
ERROR_WARNING = "ERROR: You don't have NPX installed or it's not installed correctly!"
HELP_LINK = "https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"
ERROR_INSTRUCTION = "To troubleshoot this issue, visit " + HELP_LINK

# This variable prints the success message
SUCCESS_MESSAGE = "Great! SVGO will begin optimizing the SVGs shortly..."

if platform in ("linux", "linux2"):
    # Linux
    if os.system(UNIX_COMMAND) == 0:
        print(ERROR_WARNING)
        print(ERROR_INSTRUCTION)
    else:
        print(SUCCESS_MESSAGE)
elif platform == "darwin":
    # OS X
    if os.system(UNIX_COMMAND) == 0:
        print(ERROR_WARNING)
        print(ERROR_INSTRUCTION)
    else:
        print(SUCCESS_MESSAGE)
elif platform == "win32":
    # Windows
    if os.system(WINDOWS_COMMAND) == 0:
        print(ERROR_WARNING)
        print(ERROR_INSTRUCTION)
    else:
        print(SUCCESS_MESSAGE)
