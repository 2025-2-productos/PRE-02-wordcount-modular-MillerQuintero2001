# obtain a list of files in the input directory
import os


def read_all_lines():
    input_file_list = os.listdir("data/input/")
    all_lines = []
    for filename in input_file_list:
        with open("data/input/" + filename, "r", encoding="utf-8") as f:
            all_lines.extend(f.readlines())
    return all_lines


def main():

    counter = {}
    all_lines = read_all_lines()
    for line in all_lines:
        for word in line.split():
            word = word.lower().strip(",.!?")
            counter[word] = counter.get(word, 0) + 1

    # input_file_list = os.listdir("data/input/")

    # # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_file_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    # create the directory output/ if it doesn't exist
    write_count_words(counter)


def write_count_words(counter):
    if not os.path.exists("data/output"):
        os.makedirs("data/output")

    # save the results using tsv format
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")


if __name__ == "__main__":
    main()
