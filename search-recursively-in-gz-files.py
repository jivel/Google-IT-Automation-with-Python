import pathlib
import gzip
import re
import argparse
import time
import os

fileDir = r"/home/"
fileExt = r"**\*.gz"
ENCODING = 'ISO-8859-1'

def get_without_special_chars(text):
    return text.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})

def get_name_file(text):
    return get_without_special_chars(text)+".txt"

def get_paths_gz():
    return [str(gz_path) for gz_path in pathlib.Path(fileDir).glob(fileExt)]

def remove_previous_result_search(name_file_write_result):
    if os.path.exists(name_file_write_result):
        os.remove(name_file_write_result)

def search_recursively_in_gz_files(text):
    start = time.process_time()
    name_file_write_result = get_name_file(text)
    print(name_file_write_result)
    remove_previous_result_search(name_file_write_result)
    paths_gz = get_paths_gz()
    for path_gz in paths_gz:
        write_line_if_exists_text(path_gz, text, name_file_write_result)

    stend = time.process_time()
    thetime = stend-start
    print("Finish in {} seconds".format(thetime))

def write_line_if_exists_text(path_gz, text, name_file_write_result):
    with gzip.open(filename=path_gz, mode='rt', encoding=ENCODING) as input_file:
        for line in input_file:
            #matches = re.findall(r'{}'.format(text), line)
            #if matches:
            if text in line:
                with open(name_file_write_result,"a+", encoding=ENCODING) as result_file:
                    result_file.write(line)

# Al abrir todo el archivo ocurre desbordamiento de memoria
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


