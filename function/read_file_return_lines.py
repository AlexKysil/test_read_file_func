
def read_file_return_lines(file_path, N_lines):
    """
    This function reads *.txt file by given Relative path, and print last N lines
    :param file_path: relattive file path
    :param N_lines: expected number of lines to print
    :return:
    """
    with open(file_path, "rt") as file:
        lines = file.read().splitlines()

    for row in lines[N_lines * -1:]: print(row)
