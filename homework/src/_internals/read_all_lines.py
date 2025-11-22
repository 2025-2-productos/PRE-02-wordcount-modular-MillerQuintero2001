import os


def read_all_lines():
    input_file_list = os.listdir("data/input/")
    all_lines = []
    for filename in input_file_list:
        with open("data/input/" + filename, "r", encoding="utf-8") as f:
            all_lines.extend(f.readlines())
    return all_lines
