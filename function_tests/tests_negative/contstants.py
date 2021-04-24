"""
File to save constant values for negative tests
"""

INVALID_FILE_PATHS = [
    (
        1235675, "Expected type for file_path is string, but <class \'int\'> was given."
    ),
    (
        "C//Desktop//file_2_read.txt",
        "[Errno 2] No such file or directory: 'C//Desktop//file_2_read.txt'"
    ),
    (
        "", "file_path value can not be empty, please provide valid value."
    )
]


INVALID_NLINES = [
    ("/function_tests/src/eng_file.txt", "N_lines", "Expected type for N_lines is int, but <class 'str'> was given."),
    (
        "/function_tests/src/eng_file.txt", [],
        "[Errno 2] No such file or directory: \'/Users/okysil/PycharmProjects/test_read_file_func/function_tests/tests_negative/../function_tests/src/eng_file.txt\'"
    )
]

JSON_FILE = "/function_tests/src/json_file.json"
EXPECTED_JSON_ERROR = "Expected file format is *.txt, but son was given."
