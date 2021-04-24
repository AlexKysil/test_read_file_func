''' Negative tests for read_file_return_lines function '''

import logging
import pytest

from function.read_file_return_lines import read_file_return_lines
from function_tests.tests_positive.constants import ENGLISH_TEXT, LINES_LEN_VAL, MULTIPLE_LANGUAGES, SYMBOLS_FILE, \
    EXPECTED_SYMBOLS_STR, EMPTY_FILE
from helpers.helpers_methods import construct_absolute_path
from helpers.read_terminal_output import ReadTeminalOutput

LOGGER = logging.getLogger('logger')

WHOLE_ENG_FILE_SIZE = 21


@pytest.mark.positive
def test_read_only_by_path():

    path = construct_absolute_path(ENGLISH_TEXT)

    with ReadTeminalOutput() as output:
        read_file_return_lines(path)

    assert len(output) == WHOLE_ENG_FILE_SIZE, \
        f"Expected length for English file is {WHOLE_ENG_FILE_SIZE}, but {len(output)} was found."


@pytest.mark.positive
@pytest.mark.parametrize("n_lines, expected_lines", LINES_LEN_VAL)
def test_read_file_dif_lines(n_lines, expected_lines):

    path = construct_absolute_path(ENGLISH_TEXT)

    with ReadTeminalOutput() as output:
        read_file_return_lines(path, n_lines)

    len(output)
    assert len(output) == len(expected_lines), \
        f"Actual output size: {len(output)} didn`t match to expected: {len(expected_lines)}"
    assert all(output[index] == expected_lines[index] for index in range(len(expected_lines))), \
        f"Output lines or order {''.join(output)} didn`t match to expected: {expected_lines}"


@pytest.mark.positive
@pytest.mark.parametrize("path, expected_result", MULTIPLE_LANGUAGES)
def test_read_dif_languages(path, expected_result):

    path = construct_absolute_path(path)

    with ReadTeminalOutput() as output:
        read_file_return_lines(path, 3)

    assert ''.join(output) == expected_result, \
        f"Actual output: {''.join(output)} didn`t match to expected: {expected_result}"


@pytest.mark.positive
def test_empty_doc():

    path = construct_absolute_path(EMPTY_FILE)

    with ReadTeminalOutput() as output:
        read_file_return_lines(path)

    assert not output, f'Expected empty output, but received value: {output}'


@pytest.mark.positive
def test_read_file_symbols():

    path = construct_absolute_path(SYMBOLS_FILE)

    with ReadTeminalOutput() as output:
        read_file_return_lines(path)

    assert ''.join(output) == EXPECTED_SYMBOLS_STR, \
        f"Actual symbols str: {''.join(output)} didn`t match to expected: {EXPECTED_SYMBOLS_STR}"
