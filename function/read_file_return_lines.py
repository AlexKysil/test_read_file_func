import os

def read_file_return_lines(file_path, N_lines):
    """
    This function reads *.txt file by given path, and print last N lines
    :param file_path: relattive file path
    :param N_lines: expected number of lines to print
    :return:
    """
    file_path = os.path.abspath(os.getcwd()) + file_path

    with open(file_path, "rt") as file:
        lines = file.read().splitlines()

    for row in lines[N_lines * -1:]: print(row)
