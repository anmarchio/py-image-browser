# PyImageBrowser

This little script allows to walk through a given directory and collect all image files written in python.
The list of image files is then written to an HTML file containing a sortable and searchable table with file links to simplify image file management.
The tool is designed to run platform independent.

## Setup and Configuration

Clone Repository:

`git clone https://github.com/anmarchio/image-indexer.git`

You should have a working installation of Python 3.x on your local machine. First of all, create a virtual environment in the project directory:

```
cd <project-directory>
python3 -m venv venv
```

## Run Program

Run the script using the following command:

`python main.py --dirpath <path-to-image-directory> --outpath <destination-for-index-file>`

*Note:* Do not use the same destination and input directory in order to avoid memory errors.

Use `--outpath "."` if you want to write the index HTML file to the directory which the script is executed from.

The program iterates through all directories in the given path and writes all image files to an HTML table.
Only image files will be collected which includes the following formats:

- `bmp`
- `gif`
- `jpg/jpeg`
- `png`
- `tif/tiff`

## Frameworks

The HTML page is built using a simlpe bootstrap style and jquery script. The script is based on w3school boostrap and jquery as proposed in the following tutorial: 
https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_filters_table&stacked=h