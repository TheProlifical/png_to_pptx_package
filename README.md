
# PNG to PPTX Converter

``
**Note:** This project is scheduled for archival as a more advanced version will be developed in the future. However, due to my current health, further development is temporarily on hold.
``

`png_to_pptx` is a Python package designed to convert PNG images into a PowerPoint (PPTX) presentation with a 16:9 aspect ratio. This tool is useful for quickly creating presentations from a set of PNG images.

## Features

- Converts PNG images to a PPTX presentation.
- Maintains a 16:9 aspect ratio for slides.
- Simple and easy-to-use API.

## Installation

You can install `png_to_pptx` via pip:

```bash
pip install png_to_pptx
```

## Usage

To convert PNG images to a PPTX presentation, use the `pngs_to_pptx_16x9` function. Here's a basic example:

```python
from png_to_pptx import pngs_to_pptx_16x9

# Path to the folder containing PNG images
png_folder = "path/to/png_folder"

# Path where the PPTX file will be saved
pptx_file = "path/to/output_presentation.pptx"

# Convert PNG images to PPTX
pngs_to_pptx_16x9(png_folder, pptx_file)
```

### Parameters

- `png_folder` (str): The path to the folder containing PNG images.
- `pptx_file` (str): The path where the resulting PPTX file will be saved.

## Example

Suppose you have a folder named `images` with PNG files and you want to create a PowerPoint presentation named `presentation.pptx`:

```python
from png_to_pptx import pngs_to_pptx_16x9

png_folder = "images"
pptx_file = "presentation.pptx"

pngs_to_pptx_16x9(png_folder, pptx_file)
```

This will create a PowerPoint presentation where each PNG image is placed on a slide with a 16:9 aspect ratio.

## Acknowledgements

- [python-pptx](https://python-pptx.readthedocs.io/) for handling PowerPoint file operations.
- [Pillow](https://pillow.readthedocs.io/) for image processing.


