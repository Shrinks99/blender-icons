"""
Filename:
    svg_to_yaml.py

Function:
    Generates boilerplate YAML based on icons placed in the
    `blender-icons` folder

Important notes:
    Code should be formatted by black and checked for bugs by pylint
"""

import os
import sys
import yaml
import lxml.etree as etree

# VARIABLES

# Path where the SVG icons are located
# This should not need to be changed unless
# the icons are moved somewhere else
icons_path = "../blender-icons"

# Standard width and height of an icon - nominally this is set
# to 20px by 20px

standard_width = 20
standard_height = 20

# Base tags - tags every icon would have

base_tags = ["icon", "blender"]

# FUNCTIONS

# Function to remove newlines
def purge_nl(string):
    """
    Usage: purge_nl(<your-multiline-string>)
    """
    purged_string = " ".join(string.strip().replace("\n", "").split())
    return str(purged_string)

# Function for removing the .svg extension;
# must take 1 str as input
def unextensionify(file_name: str):
    """
    Usage: unextensionify("something.svg")
    """
    return file_name.replace(".svg", "")

# Function for pretty-printing YAML;
# must take 1 dict as input
def printyaml(obj: dict):
    """
    Usage: printyaml(yourDict)
    """
    return yaml.dump(obj, sort_keys=False, default_flow_style=False)

# Function to get the innerXML of any SVG
def get_inner_xml(element):
    """
    Usage: get_inner_xml(etree.fromstring("your-xml-string"))
    """
    inner_xml = element.text + "".join(etree.tostring(e, encoding="unicode") for e in element)
    return inner_xml

# MAIN PROCESS

# First, we need to create a list with the
# names of all of the svgs in the icons_path folder
icons_list = []
for svg_icon in os.listdir(icons_path):
    icons_list.append(svg_icon)

# Second, we need to create a new dictionary to hold
# our values for every icon, which has a format like this:
#
#     "some_icon": {
#         "filename": "some_icon.svg",
#         "width": 20,
#         "height": 20,
#         "tags": ["tag1", "tag2", "tag3"]
#     }
#     "some_other_icon": {
#         "filename": "some_icon.svg",
#         ...

all_icons_dict = {}

# Then, we need to create a subdictionary for each icon,
# as we loop through our icons list. We add the filename,
# width, and tags to each subdictionary.

for icon in icons_list:
    # We set the name, filename, width, height, and tags
    # to be added as values to the subdict
    subdict_category_name = unextensionify(icon)
    filename = icon
    width = standard_width
    height = standard_height
    tags = base_tags
    svg_rawtext = open(os.path.join("../blender-icons", filename), "r").read()
    # Parses the SVG like an XML document so it can be manipulated with etree
    svg_parsed = etree.fromstring(svg_rawtext)
    # We just need to extract everything inside the <svg> tag
    # as we're replacing the default viewBox and fills with custom
    # values anyways (based on data from the YAML file) and we
    # clean the extracted string for newlines and empty spaces
    svg_textcontent = purge_nl(str(get_inner_xml(svg_parsed)))
    # We enclose the innercontent in a <g> tag
    # This is to prevent an lxml error in which svg
    # markup without 1 single svg root tag is invalid
    # reference: https://stackoverflow.com/questions/16972737/
    svg_content = purge_nl(r"<g>" + svg_textcontent + r"</g>")
    # We create a dictionary for each icon to store the parsed data
    icons_subdict = {
            "filename": filename,
            "label": subdict_category_name,
            "width": width,
            "height": height,
            "tags": list(tags),
            "markup": svg_content
        }
    # We store this data as a key-value pair in our final_icons dict
    all_icons_dict[subdict_category_name] = icons_subdict

# Last, we simply need to print out the results as YAML
print("Generated YAML:")
print(printyaml(all_icons_dict))
# We ask the user if the results should be saved to a YML file
print("Would you like to save the results to a YAML file? (Recommended)")
answer = input("[Y/N]: ")
if answer in ("Y", "y"):
    with open("generated-icons-data.yml", "w") as new_file:
        new_file.write(printyaml(all_icons_dict))
    print("Success! YAML data written to ./generated-icons-data.yml")
else:
    print("Results not saved. Exiting...")
    sys.exit()
