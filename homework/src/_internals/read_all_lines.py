import os


def read_all_lines(input_folder: str):
    input_file_list = os.listdir(input_folder)
    all_lines = []
    for filename in input_file_list:
        with open(input_folder + filename, "r", encoding="utf-8") as f:
            all_lines.extend(f.readlines())
    return all_lines
