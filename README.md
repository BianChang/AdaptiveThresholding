# AdaptiveThresholding

AdaptiveThresholding is a Python package designed for reproducible and systematic thresholding in multiplex immunohistochemistry (mIHC) and immunofluorescence (mIF) image analysis. This tool applies an adaptive thresholding method, optimized to define cell positivity by combining an initial Otsu threshold with a Bayesian Gaussian Mixture Model (BGMM) approach. By automating the thresholding process, AdaptiveThresholding enables efficient analysis of complex image datasets for diagnostic and prognostic research applications.

## Features
- Adaptive thresholding method (Otsu + BGMM) for robust cell positivity detection.
- Designed for mIHC/mIF image analysis with easily configurable marker selection.
- Export results as new CSVs with thresholding data for downstream analysis.
- Supports efficient, batch processing of multiple images.

## Installation

First, clone this repository and navigate to its root directory:
```bash
git clone https://github.com/your-username/AdaptiveThresholding.git
cd AdaptiveThresholding
```
Then, install the package with pip:
```bash
pip install .
```

#Usage
AdaptiveThresholding processes CSV files containing marker intensity data and adds thresholded results for each specified marker.
## Command-Line Interface
Run the tool using the command line:
```bash
python -m adaptive_thresholding.main <input_folder> <output_folder> --marker_columns <marker1> <marker2> ...
```
#### Arguments
- `<input_folder>`: Path to the folder containing input CSV files.
- `<output_folder>`: Path to the folder where output CSV files will be saved.
- `--marker_columns`: Names of the columns to apply thresholding, separated by spaces.

Example:
```bash
python -m adaptive_thresholding.main ./data/input ./data/output --marker_columns CD4 CD3 CD20
```


