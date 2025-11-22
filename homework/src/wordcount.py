# obtain a list of files in the input directory
import os

# from homework.src.write_count_words import write_count_words
from ._internals.write_count_words import write_count_words


def read_all_lines():
    input_file_list = os.listdir("data/input/")
    all_lines = []
    for filename in input_file_list:
        with open("data/input/" + filename, "r", encoding="utf-8") as f:
            all_lines.extend(f.readlines())
    return all_lines


# def main():

#     # counter = {}
#     # all_lines = read_all_lines()
#     # for line in all_lines:
#     #     for word in line.split():
#     #         word = word.lower().strip(",.!?")
#     #         counter[word] = counter.get(word, 0) + 1

#     all_lines = []
#     input_files_list = os.listdir("data/input/")
#     for filename in input_files_list:
#         file_path = os.path.join("data/input/", filename)
#         with open(file_path, "r", encoding="utf-8") as f:
#             all_lines.extend(f.readlines())

#     all_lines = [line.strip().lower() for line in all_lines]

#     words = []
#     for line in all_lines:
#         words.extend(line.strip(",.!?") for words in line.split())

#     # count words
#     counter = {}
#     for word in words:
#         counter[word] = counter.get(word, 0) + 1

#     # input_file_list = os.listdir("data/input/")

#     # # count the frequency of the words in the files in the input directory
#     # counter = {}
#     # for filename in input_file_list:
#     #     with open("data/input/" + filename) as f:
#     #         for l in f:
#     #             for w in l.split():
#     #                 w = w.lower().strip(",.!?")
#     #                 counter[w] = counter.get(w, 0) + 1

#     write_count_words(counter)


def main():
    ## read all lines
    all_lines = []
    input_files_list = os.listdir("data/input/")
    for filename in input_files_list:
        file_path = os.path.join("data/input", filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)

    ### preprocess lines
    all_lines = [line.strip().lower() for line in all_lines]

    ### split in words
    words = []
    for line in all_lines:
        words.extend(words.strip(",.!?") for words in line.split())

    ### count words
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_files_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    write_count_words(counter)


if __name__ == "__main__":
    main()
