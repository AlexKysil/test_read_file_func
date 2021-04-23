import atexit
import datetime
import pytest
import os
import sys
import re

from logging.handlers import MemoryHandler
from logging import getLogger, StreamHandler, INFO, Formatter, CRITICAL, DEBUG, shutdown

LOGGER = getLogger('logger')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''This hook is to get test status(failed/passed) for test'''
    outcome = yield
    rep = outcome.get_result()

    if call.when == 'teardown':
        LOGGER.info(
            f"Test: {item._nodeid} Result: {rep.outcome},  \
            Exception:{call.excinfo.typename if call.excinfo else ''} {call.excinfo.value if call.excinfo else ''}")


@pytest.fixture(scope="function", autouse=True)
def logger_fixture(request):
    """Create logger for each thread"""
    memory_handler = None
    logger = None
    if hasattr(request.config, 'slaveinput'):
        memory_handler, logger = create_logger_process(request)

    yield memory_handler

    if memory_handler:
        LOGGER.debug('temorary debug: stream flushed')
        memory_handler.flush()
        del logger


@pytest.fixture(scope="session", autouse=True)
def create_logger(request):
    """Creating custom logger for each test"""
    if not os.getenv('PYTEST_XDIST_WORKER_COUNT', None) and not any(it for it in sys.argv if re.match('^-n', it)):
        logger = getLogger("logger")
        logger.setLevel(DEBUG)
        console_handler = StreamHandler()
        console_handler.name = str(datetime.datetime.now().microsecond)
        console_handler.setLevel(INFO)
        # create formatter
        formatter = Formatter(
            console_handler.name + " %(asctime)s - %(filename)s - %(levelname)s - %(message)s")
        # add formatter to console_handler
        console_handler.setFormatter(formatter)
        # add console_handler to logger
        logger.addHandler(console_handler)


def create_logger_process(request):
    """
    Create logger for process
    :param request:
    :return:
    """
    logger = getLogger("logger")
    logger.setLevel(INFO)

    console_handler = StreamHandler(sys.stderr)
    console_handler.setLevel(INFO)
    formatter = Formatter("%(stream_name)s %(asctime)s - %(filename)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    memory_handler = MemoryHandler(1024 * 3000, flushLevel=CRITICAL, target=console_handler)
    logger.addHandler(memory_handler)
    atexit.register(shutdown)

    return memory_handler, logger
