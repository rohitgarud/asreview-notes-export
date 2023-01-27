[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![PyPI version](https://badge.fury.io/py/asreview-notes-export.svg)](https://badge.fury.io/py/asreview-notes-export)

# ASReview Notes Export Extension
This is a simple extension for [ASReview](https://github.com/asreview) ![logo](https://raw.githubusercontent.com/asreview/asreview-artwork/e2e6e5ea58a22077b116b9c3d2a15bc3fea585c7/SVGicons/IconELAS/ELASeyes24px24px.svg "ASReview") that can be used to export notes from the ASReview GUI while exporting the labeled or partially labeled dataset as .csv file.

## Installation
ASReview notes-export can be installed from PyPI:
```bash
pip install asreview-notes-export
```

After installation, check if the `asreview-notes-export` package is listed as an
extension. Use the following command:

```bash
asreview --help
```

It should list the `notes_export` subcommand.

## Usage
To export all the records from the dataset with the current state of labels and notes, we can use the following command:
```
asreview notes_export YOUR_ASREVIEW_FILE.asreview
```

To export only the records with notes from the dataset, we can use the following command:
```
asreview notes_export --only-with-notes YOUR_ASREVIEW_FILE.asreview
```

The filename of the output .csv is the same as the name of .asreview file. To save the output to .csv file with a custom filename, we can use the following command. We can either specify the extension:
```
asreview notes_export --only-with-notes YOUR_ASREVIEW_FILE.asreview -o YOUR_OUTPUT_FILENAME.csv
```  

or only the filename will suffice, without an extension, using the following command:
```
asreview notes_export --only-with-notes YOUR_ASREVIEW_FILE.asreview -o YOUR_OUTPUT_FILENAME
``` 

Note that currently only .csv output is supported. 

## License
The extension is published under the [Apache 2.0 license](https://github.com/rohitgarud/asreview-notes-export/blob/main/LICENSE).

## Contact
This is an unofficial extension of ASReview and is developed and maintained by [Rohit Garud](https://github.com/rohitgarud). 

