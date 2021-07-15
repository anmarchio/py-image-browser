import argparse

from create_index import create_index

DIR_PATH = ""
OUTPUT_PATH = ""

# --directory "Q:\5 Fachbereiche\03 OPM" --output "Q:\5 Fachbereiche\03 OPM"
# --directory "C:\Users\mara_c10\Desktop\ReferenzSet" --output "C:\Users\mara_c10\Desktop\ReferenzSet"

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
    DIR_PATH, OUTPUT_PATH = store_values(args)

    print("---------------------------")
    print("Create HTML Directory Index")
    print("---------------------------")
    create_index(DIR_PATH, OUTPUT_PATH)
