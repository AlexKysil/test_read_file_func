'''
File for test helper methods
'''

import os


def construct_absolute_path(relative_path):
    """
    Helper method which recieves relative path and add necessary part
    :param relative_path:
    :return:
    """

    return ''.join([os.path.abspath(os.curdir), '/../', relative_path])
