# Blender Icons

Up to now Blender's icons have all been stored in a big SVG file [over here](https://developer.blender.org/diffusion/B/browse/master/release/datafiles/blender_icons.svg).  I don't like this method, it's hard to find things unless you know exactly where they are because the file isn't searchable and the layers aren't named.

**This project aims to store the Blender icons in a friendlier, more intuitive manner**. Check out the icons [here](https://wilkinson.graphics/Blender-Icons))!

- [Download](https://github.com/Shrinks99/blender-icons/releases) (nicely packaged downloads are coming soon! 👀)
- [Goals](#goals)
- [Contributing](#contributing)
- [How to use](#how-to-use)
- [Licensing](#license)

## Goals

This repository was created with the goal of organizing Blender's massive icon SVG into individually named files.  Files are named based on what Blender calls the icon in its icon viewer. As a result of this hugely manual porting process, SVGs are cleaned up wherever possible.

Some new icons adhering to the same styles and rules set by Blender's developers will also be created.  The idea is to generalize the set so that it may be used in other similar creative applications.  Any new icons created will be tagged in the YAML file as `bonus`.

## Contributing

For those who wish to contribute, Blender's icons adhere to a 20×20px grid with 4px of padding on each side.  Icons must work in a single colour and transparency is used to create different shades.  Try to keep your shapes within this pixel grid, any stroke lines should most likely be 1px wide.

Any added icons must also added as an entry to the to the `icons-list.yml` file!

For whatever reason some icons that were in the sheet weren't able to be found in Blender's icon browser.  Do you know what the icons in the `uncategorized` folder should be named (according to Blender's names)?  Have you got _proof?_  Make an issue and let me know!

## How to use

The easiest way to browse icons included in Blendicons is to use the web-based viewer at [https://wilkinson.graphics/blender-icons](https://wilkinson.graphics/blender-icons).

If you wish to download the whole set you can do so by clicking on the green "Code" button and selecting "Download ZIP from the dropdown menu."

## Development

To make changes to Blendicons, first clone the repository to your local machine:

```bash
git clone https://github.com/shrinks99/Blender-Icons.git && cd Blender-Icons
```

Next, `cd` into the `docs/` folder:

```bash
cd Blender-Icons
```

The following instructions are for developing the web viewer and icon processing scripts. If you simply want to look through the icons, follow the instructions in *"How to use"*.

We are assuming you have either `GNU Make` or `nmake` on your machine. If that's not the case, go install that! Once you do so, you can begin modifying the sources. A full list of options for the Makefile can be found by simply running `make`.

The web viewer uses TailwindCSS for styling but is written entirely in HTML and vanilla JavaScript. To make a development build (non-optimized, so you'll be generating a huge CSS file), run `make generate` then `make dev` and lastly `make serve`.  Note that the Python maodule `markdown2` is required, to install it use `pip install markdown2`.

To make a production-ready build, run `make generate && make dist`. With luck (using either approach), you should now see a local copy of Blendicons' website in your browser at <http://localhost:8080>!

## License

Blender's icons are released under a [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.  Any additional icons that have been added are also released under this license.
