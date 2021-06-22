"""
Filename:
    replacer.py

Function:
    Cleans up extraneous style="..." attributes from SVG markup
    and replaces the styles with one unified fill attribute

Important notes:
    Code should be formatted by black and checked for bugs by pylint
"""
import re
import os, sys
# Takes a folder name as input
# E.g. cat somefile.svg | replacer.py

# VARIABLES

# Counters for adjusting replacer.py
# to operate in directory or file mode
isDir = False
isFile = False

subst_style = 'fill="#ffffff"'
# Regex grabs the equivalent of 'style="*"'
# essentially this finds 
regex = r'style="(.*?)"'

# New appended extension for converted svg
# Typically this should be disabled
new_ext = False

# If new append extension is enabled,
# this is the new appended extension
new_ext_name = ".new.svg"

# FUNCTIONS

# Function for removing the .svg extension;
# must take 1 str as input
def unextensionify(file_name: str):
    """
    Usage: unextensionify("something.svg")
    """
    return file_name.replace(".svg", "")

# Function for printing the usage guide
# No inputs
def help_message():
    print("Example usage:")
    print("\tpython replacer.py my_folder_of_svgs")
    print("\tpython replacer.py my_icon.svg\n")

# MAIN PROCESS

# Check that the user entered arguments correctly
# and warn the user if the arguments were incorrect
if len(sys.argv) < 2:
    help_message()
    print("You forgot to enter arguments!")
    sys.exit()
else:
    source = sys.argv[1]
    if os.path.isdir(source):
        print("In your folder, these svgs were found:\n")
        for item in os.listdir(source):
            # We want to print a newline after the last
            # SVG file for nicer-looking output
            if item == os.listdir(source)[-1]:
                print("- {}\n".format(item))
            else:
                # Print each SVG in list view
                print("- {}".format(item))
        # Set to directory mode
        isDir = True
    elif os.path.isfile(source):
        print("Your input SVG:", source, "\n")
        # Set to file mode
        isFile = True
    else:
        help_message()
        print("Your input was invalid!")

# Begin the replacement
# and also adjust the replacement method
# via whether file mode or folder mode is enabled
if isDir:
    for icon in os.listdir(source):
        svg_path = source + icon
        print("Processing {}".format(svg_path))
        with open(svg_path, "r") as svg:
            svg_content = svg.read()
            # Replace that big ugly block of styles to the clean fill attribute
            # and write the cleaned-up SVG to a string called "result"
            result = re.sub(regex, subst_style, svg_content, 0, re.MULTILINE)
        # Print output if successful
        if result:
            if new_ext:
                result_filename = unextensionify(svg_path) + new_ext_name
            else:
                result_filename = svg_path
            print("Writing cleaned-up markup to {}...".format(result_filename))
            with open(result_filename, "w") as output:
                output.write(result)
            print("Done!\n")
        else:
            print("ERROR Regex substitution failed.")
elif isFile:
    with open(source, "r") as svg:
        svg_content = svg.read()
        # Replace that big ugly block of SVG style to the clean fill attribute
        result = re.sub(regex, subst_style, svg_content, 0, re.MULTILINE)
        # Print output if successful
        if result:
            print(result)
            print("\nWriting cleaned-up markup...")
            result_filename = unextensionify(source) + ".new.svg"
            with open(result_filename, "w") as output:
                output.write(result)
        else:
            print("ERROR Regex substitution failed.")
