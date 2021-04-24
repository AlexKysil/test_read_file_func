''' Negative tests for read_file_return_lines function '''

import logging
import pytest

from function.read_file_return_lines import read_file_return_lines
from function_tests.tests_negative.contstants import INVALID_FILE_PATHS, INVALID_NLINES
from helpers.helpers_methods import construct_absolute_path
from helpers.read_terminal_output import ReadTeminalOutput

LOGGER = logging.getLogger('logger')


@pytest.mark.negative
@pytest.mark.parametrize("path, expected_error", INVALID_FILE_PATHS)
def test_read_by_wrong_path(path, expected_error):

    try:
        with ReadTeminalOutput() as output:
            read_file_return_lines(path)
    except(TypeError, ValueError, FileNotFoundError) as ex:
        assert str(ex) == expected_error


@pytest.mark.negative
@pytest.mark.parametrize("valid_path, n_lines, expected_error", INVALID_NLINES)
def test_read_with_wrong_nlines(valid_path, n_lines, expected_error):

    valid_path = construct_absolute_path(valid_path)

    try:
        with ReadTeminalOutput() as output:
            read_file_return_lines(valid_path, n_lines)
    except(TypeError, FileNotFoundError) as ex:
        assert str(ex) == expected_error



def test_not_txt():
    pass


