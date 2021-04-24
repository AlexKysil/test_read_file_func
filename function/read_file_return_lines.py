
# pylint: disable=f-string-without-interpolation
def read_file_return_lines(file_path, N_lines=None):
    """
    This function reads *.txt file by given absolute path, and print last N lines
    :param file_path: absolute file path
    :param N_lines: expected number of lines to print
    :return:
    """

    if not file_path:
        raise ValueError('file_path value can not be empty, please provide valid value.')

    if not isinstance(file_path, str):
        raise TypeError(f'Expected type for file_path is string, but {type(file_path)} was given.')

    if N_lines:
        if not isinstance(N_lines, int):
            raise TypeError(f'Expected type for N_lines is int, but {type(N_lines)} was given.')


    with open(file_path, "rt") as file:
        lines = file.read().splitlines()

    if not N_lines or N_lines == 0:
        for row in lines: print(row)
    elif N_lines > 0:
        for row in lines[N_lines * -1:]: print(row)
    elif N_lines < 0:
        for row in lines[N_lines:]: print(row)
