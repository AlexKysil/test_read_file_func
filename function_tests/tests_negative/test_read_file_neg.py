''' Negative tests for read_file_return_lines function '''

import logging
import pytest

from function.read_file_return_lines import read_file_return_lines
from function_tests.tests_negative.contstants import INVALID_FILE_PATHS, INVALID_NLINES, JSON_FILE, EXPECTED_JSON_ERROR
from helpers.helpers_methods import construct_absolute_path
from helpers.read_terminal_output import ReadTeminalOutput

LOGGER = logging.getLogger('logger')


@pytest.mark.negative
@pytest.mark.parametrize("path, expected_error", INVALID_FILE_PATHS)
def test_read_by_wrong_path(path, expected_error):

    try:
        with ReadTeminalOutput():
            read_file_return_lines(path)
    except(TypeError, ValueError, FileNotFoundError) as ex:
        assert str(ex) == expected_error, \
            f'Actual Error for expected wrong File Path: {expected_error}, didn`t match: {ex}'


@pytest.mark.negative
@pytest.mark.parametrize("valid_path, n_lines, expected_error", INVALID_NLINES)
def test_read_with_wrong_nlines(valid_path, n_lines, expected_error):

    valid_path = construct_absolute_path(valid_path)

    try:
        with ReadTeminalOutput():
            read_file_return_lines(valid_path, n_lines)
    except(TypeError, FileNotFoundError) as ex:
        assert str(ex) == expected_error, \
            f"Error for wrong N_lines value didn`t match to expected: {expected_error}, actual value: {ex}"


@pytest.mark.negative
def test_read_not_txt():

    path = construct_absolute_path(JSON_FILE)

    try:
        with ReadTeminalOutput():
            read_file_return_lines(path)
    except(ValueError) as ex:
        assert str(ex) == EXPECTED_JSON_ERROR, \
            f'Received error didn`t match to expected Wrong Format: {EXPECTED_JSON_ERROR}. Exception: {ex}.'
