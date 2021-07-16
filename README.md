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

Make sure to install all local requirements using:

`pip install -r requirements.txt`

Then run the script using the following command:

`python main.py --dirpath <path-to-image-directory> --outpath <destination-for-index-file>`

## Code basis

The following style and page logic has been used for implementation:

https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_filters_table&stacked=h