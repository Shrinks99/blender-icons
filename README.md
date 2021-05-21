# Blender Icons

Up to now Blender's icons have all been stored in a big SVG file [over here](https://developer.blender.org/diffusion/B/browse/master/release/datafiles/blender_icons.svg).  I don't like this method, it's hard to find things unless you know exactly where they are because the file isn't searchable and the layers aren't named.

**This project aims to store the Blender icons in a friendlier, more intuitive manner**. Check out the icons [here](./blender-icons/sets/Lcn-NIS8Eh8o)!

- [Download](https://github.com/Shrinks99/blender-icons/releases) (nicely packaged downloads are coming soon! 👀)
- [Goals](#goals)
- [Contributing](#contributing)
- [How to use](#how-to-use)
- [Licensing](#license)

## Goals

This repository was created with the goal of organizing Blender's massive icon SVG into individually named files.  Files are named based on what Blender calls the icon in its icon viewer. As a result of this hugely manual porting process, SVGs are cleaned up wherever possible.

Some new icons adhering to the same styles and rules set by Blender's developers will also be created.  The idea is to generalize the set so that it may be used in other similar creative applications.  Any new icons created will be tagged in the Iconset database as `bonus`.

## Contributing

For those who wish to contribute, Blender's icons adhere to a 20×20px grid with 4px of padding on each side.  Icons must work in a single colour and transparency is used to create different shades.  Try to keep your shapes within this pixel grid, any stroke lines should most likely be 1px wide.

_Do not edit the database or import icons into Iconset yourself!_  This program isn't amazing for team or git collaboration and it's kinda hard to track changes because the json it creates is minified and it doesn't seem to add data in an iterative way.  Instead, move your icons into an `ingest` folder in the repository root directory!  If you are submitting any icons that aren't already present in Blender please note these in your PR.  I will move icons out of this folder once they've been reviewed and import them into the directory myself at the end of the review process.

## How to use

This repository is best used with [Iconset](https://iconset.io/), a freeware icon management application for macOS and Windows.  Download the program, open its preferences, and hit the `switch` button to select the `blender-icons` folder _within_ this repository (do not select the repo itself).  Note that you must be using dark mode to actually see the icons as they're all white!  When possible icons are tagged for easy searching.

If you don't feel like installing anything you can just browse to `blender-icons/sets/Lcn-NIS8Eh8o` to find all the individual SVG files.

## License

Blender's icons are released under a [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.  Any additional icons that have been added are also released under this license.
