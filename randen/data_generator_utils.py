"""
pandas_data_generator.randen.utils.py:
    Utilites
"""

__author__ = "Kanishk Varshney"
__date__ = "05-10-2020"
__appname__ = "pandas_data_generator"

import os
import configparser

import logging
logger = logging.getLogger(__appname__)

def get_config(section, option):
    """[summary]

    Args:
        section ([type]): [description]
        option ([type]): [description]

    Raises:
        ValueError: [description]
        ValueError: [description]

    Returns:
        [type]: [description]
    """
    config_path = "config.ini"
    config_path = os.path.join(os.path.dirname(__file__), config_path)

    config = configparser.ConfigParser()
    config.read(config_path)

    if not config.has_section(section):
        raise ValueError('%s has no section %s' % (config_path, section))

    if not config.has_option(section, option):
        raise ValueError('%s has no option %s in section %s' % (config_path, option, section))

    return config.get(section, option)
