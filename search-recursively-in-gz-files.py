import pathlib
import gzip
import re
import argparse

fileDir = r"/home/"
fileExt = r"**\*.gz"
ENCODING = 'ISO-8859-1'

def get_paths_gz():
    return [str(gz_path) for gz_path in pathlib.Path(fileDir).glob(fileExt)]


def search_recursively_in_gz_files(text):
    paths_gz = get_paths_gz()
    total = 0
    for path_gz in paths_gz:
        total += find_text_in_gz_file(path_gz, text)
    print("Total: {}".format(total))

def find_text_in_gz_file(path_gz, text):
    with gzip.open(filename=path_gz, mode='rt', encoding=ENCODING) as input_file:
        all_data = input_file.read()
        lines = re.findall(r'{}'.format(text), all_data)
        if lines:
            print('Total: {} Path file: {}'.format(len(lines), path_gz))
            return len(lines)
        return 0

parser = argparse.ArgumentParser()
parser.add_argument("--text", "-t")
args = parser.parse_args()

if args.text:
    print("searching {} in {}".format(args.text, fileDir))
    search_recursively_in_gz_files(args.text)
