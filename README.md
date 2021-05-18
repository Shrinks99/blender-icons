# Blender Icons

Up to now Blender's Icons have all been stored in a big SVG file [over here](https://developer.blender.org/diffusion/B/browse/master/release/datafiles/blender_icons.svg).  I don't like this method, it's hard to find things unless you know exactly where they are because the file isn't searchable and the layers aren't named.

## Goals

This repository was created with the eventual goal of breaking _all_ of these icons out of this SVG and organizing them in individually named files.  Files are named based on what Blender calls the icon in its icon viewer.  As a result of this hugely manual porting process I also intend to clean things up where possible.

I may create some new icons adhering to the same styles and rules set by Blender's developers.  The idea is to generalize the set so that it may be used in other similar creative applications.

## Contributing

For those who wish to contribute, Blender's icons adhere to a 20×20px grid with 4px of padding on each side.  Icons must work in a single colour and transparency is used to create different shades.  Try to keep your shapes within this pixel grid, any stroke lines should most likely be 1px wide.

## How to use

This repository is best used with [Iconset](https://iconset.io/), a freeware icon management application for macOS and Windows.  Download the program, open its preferences, and hit the `switch` button to select this icon library.  Note that you must be using dark mode to actually see the icons as they're all white!  When possible I try to tag icons for easy searching.

If you don't feel like installing anything you can just browse to `blender-icons/sets/Lcn-NIS8Eh8o` to find all the individual SVG files.

## License

Blender's icons are released under a [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.  Any additional icons I've added are also released under this license.