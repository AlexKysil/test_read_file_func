''' Negative tests for read_file_return_lines function '''

import logging
import pytest

from function.read_file_return_lines import read_file_return_lines
from helpers.read_terminal_output import ReadTeminalOutput

LOGGER = logging.getLogger('logger')


@pytest.mark.negative
def read_by_wrong_path(path):

    with ReadTeminalOutput() as output:
        read_file_return_lines(path)

    assert output


@pytest.mark.negative
def read_with_wrong_nlines(valid_path, n_lines):

    with ReadTeminalOutput() as output:
        read_file_return_lines(valid_path)

    assert output
