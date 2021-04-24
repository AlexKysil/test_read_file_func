""" Doc for helper methods """

import sys
from io import StringIO


# pylint: disable=attribute-defined-outside-init
class ReadTeminalOutput(list):
    """
    This is helper class - context manager to read terminal output
    """
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout
