import argparse
import os
from settings import DEFAULT_FILE_NAME, HTML_HEAD, BODY_HEAD, BODY_CLOSE_TAG, QUERY_SCRIPT, IMAGE_FILE_FORMATS


def traverse_file_tree(source_path, target_path):
    for item in os.listdir(source_path):
        if os.path.isdir(os.path.join(source_path, item)):
            traverse_file_tree(os.path.join(source_path, item), target_path)
        else:
            print(os.path.join(source_path, item))
            file = os.path.splitext(item)
            if len(file) > 1 and file[1] in IMAGE_FILE_FORMATS:
                html = "<tr>\n" + \
                       "<td>" + source_path + "</td>\n" + \
                    "<td>" + item + "</td>\n" + \
                    "</tr>\n"
                f = open(os.path.join(target_path, DEFAULT_FILE_NAME), "a")
                f.write(html)
                f.close()


def generate_html(source_path, target_path):
    """
    HTML code has been adapted from:
    https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_filters_table&stacked=h

    :param source_path:
    :param target_path:
    :return:
    """
    # Loop through Folders and Create index details
    f = open(os.path.join(target_path, DEFAULT_FILE_NAME), "w")
    f.write(HTML_HEAD +
            BODY_HEAD)
    f.close()
    print("Browse directory ...")
    traverse_file_tree(source_path, target_path)
    # Write HTML code to file
    print("Finish file ...")
    f = open(os.path.join(target_path, DEFAULT_FILE_NAME), "a")
    f.write(BODY_CLOSE_TAG +
            QUERY_SCRIPT)
    f.close()


def generate_file_list(read_from, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path, mode=777)
    # Creates HTML file image_index.html
    generate_html(read_from, output_path)


def parse_and_store_arguments():
    # Initiate the parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="directory path with image files to read")
    parser.add_argument("-o", "--output", help="destination path for index file")

    # Read arguments from the command line and print them
    args = parser.parse_args()
    print_arguments(args)
    return args


def print_arguments(args):
    if args.directory:
        print("input directory          | " + str(args.directory))
    if args.output:
        print("destination directory    | " + str(args.output))


def store_values(args):
    dir = ""
    out = ""
    if args.directory:
        dir = args.directory
    if args.output:
        out = args.output
    return dir, out


if __name__ == '__main__':
    args = parse_and_store_arguments()
    dir_path, output_path = store_values(args)
    print("---------------------------")
    print("Create HTML Directory Index")
    print("---------------------------")
    generate_file_list(dir_path, output_path)
