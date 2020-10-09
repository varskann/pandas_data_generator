"""
pandas_data_generator.randen.randen.py:
    Generates random dataframe with string, int, float, etc column types
"""

__author__ = "Kanishk Varshney"
__date__ = "05-10-2020"
__appname__ = "pandas_data_generator"

import time
import random
from datetime import datetime
from typing import List
import logging

import secrets
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from functools import partial
import numpy as np
import pandas as pd

from random import random, choice


logging_format = "%(asctime)s [%(levelname)s] %(name)s : %(message)s in %(pathname)s:%(lineno)d"
logging.basicConfig(level=logging.DEBUG, format=logging_format)
logger = logging.getLogger(__appname__)


class DataFrameGenerator:
    """Dataframe Generator class
    """
    def __init__(self):
        self._numrows = None

    @staticmethod
    def _timeit(func):
        def timed(*args, **kwargs):
            start = time.time()
            for _ in range(100):
                func(*args, **kwargs)
            end = time.time()
            return end - start
        return timed

    def _generate_ints(self, _min: int = -100000, _max: int = 100000) -> np.ndarray:
        return np.random.randint(low=_min, high=_max, size=self._numrows)

    def _generate_floats(self, _min: float = -1.0, _max: float = 1.0) -> np.ndarray:
        return ((_max - _min) * np.random.random(size=self._numrows)) + _min

    def _generate_strings(self, _min: int = 10, _max: int = 20) -> List[str]:
        keys = set()
        pickchar = partial(secrets.choice, ascii_letters + digits)
        while len(keys) < self._numrows:
            keys |= {''.join([pickchar()
                              for _ in range(np.random.randint(low=_min, high=_max))])
                     for _ in range(self._numrows - len(keys))}
        return list(keys)

    def _generate_dates(self, start: datetime = None, end: datetime = None) -> pd.DatetimeIndex:
        if not start:
            start = datetime.fromtimestamp(0)
        if not end:
            end = datetime.now()
        return pd.date_range(start=start, end=end, periods=self._numrows)

    def _generate_bools(self):
        return [not random() >= 0.5 for _ in range(self._numrows)]

    def _generate_chars(self, lowercase: bool = True):
        # if lowercase:
        #    min_lc = ord(b'a')
        # else:
        #     min_lc = ord(b'A')
        # len_lc = 26
        # ba = bytearray(os.urandom(self._numrows))
        # for i, b in enumerate(ba):
        #     ba[i] = min_lc + b % len_lc  # convert 0..255 to 97..122
        # print(ba)
        # sys.stdout.buffer.write(ba)
        # return ["a"]

        # if lowercase:
        #     bal = [c.encode('ascii') for c in ascii_lowercase]
        # else:
        #     bal = [c.encode('ascii') for c in ascii_uppercase]
        # return [choice(bal) for _ in range(self._numrows)]
        if lowercase:
            return [choice(ascii_lowercase) for _ in range(self._numrows)]
        else:
            return [choice(ascii_uppercase) for _ in range(self._numrows)]

    def get_dataframe(self, nrows: int, ctypes: List[type], columns=None) -> pd.DataFrame:
        assert ctypes is not None, "provide columns' data types"
        if columns is not None:
            assert len(columns) == len(ctypes), "provide all or No Columns names"

        self._numrows = nrows
        out_df = pd.DataFrame()
        for i, _ctype in enumerate(ctypes):
            _col_name = columns[i] if columns is not None else f"{_ctype.__name__.capitalize()}"
            if _ctype == int:
                _data_list = self._generate_ints()
            elif _ctype == float:
                _data_list = self._generate_floats()
            elif _ctype == bool:
                _data_list = self._generate_bools()
            elif _ctype == str:
                _data_list = self._generate_strings()
            elif _ctype == bytes:
                _data_list = self._generate_chars()
            elif _ctype == datetime:
                _data_list = self._generate_dates()
            else:
                logger.error(f"Found unsuported {_ctype}")
                raise ValueError("Only ")

            out_df[_col_name] = _data_list

        return out_df

    def get_integer_dataframe(self, nrows: int, ncols: int, nullratio=0, columns=None,
                              minval: int = -100000, maxval: int = 100000) -> pd.DataFrame:
        if columns is not None:
            assert len(columns) == ncols, "provide all or No Columns names"

        logger.info(f"Generating {nrows}x{ncols} all integer dataframe")
        self._numrows = nrows

        out_df = pd.DataFrame()
        for i in range(ncols):
            _col_name = columns[i] if columns is not None else f"Integer{i}"
            out_df[_col_name] = self._generate_ints(_min=minval, _max=maxval)

        return out_df

    def get_float_dataframe(self, nrows: int, ncols: int, nullratio: float = 0, columns: List[str] = None,
                            minval: float = -1.0, maxval: float = 1.0) -> pd.DataFrame:
        if columns is not None:
            assert len(columns) == ncols, "Provide all or No Columns names"

        logger.info(f"Generating {nrows}x{ncols} all float dataframe")
        self._numrows = nrows

        out_df = pd.DataFrame()
        for i in range(ncols):
            _col_name = columns[i] if columns is not None else f"Float{i}"
            out_df[_col_name] = self._generate_floats(_min=minval, _max=maxval)

        return out_df

    def get_boolean_dataframe(self, nrows: int, ncols: int, nullratio=0, columns=None) -> pd.DataFrame:
        if columns is not None:
            assert len(columns) == ncols, "Provide all or No Columns names"

        logger.info(f"Generating {nrows}x{ncols} all boolean dataframe")
        self._numrows = nrows

        out_df = pd.DataFrame()
        for i in range(ncols):
            _col_name = columns[i] if columns is not None else f"Bool{i}"
            out_df[_col_name] = self._generate_bools()

        return out_df

    def get_char_dataframe(self, nrows: int, ncols: int, nullratio: float = 0, columns: List[str] = None,
                           lowercase: bool = True) -> pd.DataFrame:
        if columns is not None:
            assert len(columns) == ncols, "Provide all or No Columns names"

        logger.info(f"Generating {nrows}x{ncols} all character dataframe")
        self._numrows = nrows

        out_df = pd.DataFrame()
        for i in range(ncols):
            _col_name = columns[i] if columns is not None else f"Char{i}"
            out_df[_col_name] = self._generate_chars(lowercase=lowercase)

        return out_df

    def get_string_dataframe(self, nrows: int, ncols: int, nullratio: float = 0, columns: List[str] = None,
                             minstrlen: int = 10, maxstrlen: int = 20) -> pd.DataFrame:
        if columns is not None:
            assert len(columns) == ncols, "Provide all or No Columns names"

        logger.info(f"Generating {nrows}x{ncols} all string dataframe")
        self._numrows = nrows

        out_df = pd.DataFrame()
        for i in range(ncols):
            _col_name = columns[i] if columns is not None else f"Str{i}"
            out_df[_col_name] = self._generate_strings(_min=minstrlen, _max=maxstrlen)

        return out_df.astype(str)

    def get_dates_dataframe(self, nrows: int, ncols: int, nullratio: float = 0, columns: List[str] = None,
                            start: datetime = None, end: datetime = None) -> pd.DataFrame:
        if columns is not None:
            assert len(columns) == ncols, "Provide all or No Columns names"

        logger.info(f"Generating {nrows}x{ncols} all dates dataframe")
        self._numrows = nrows

        out_df = pd.DataFrame()
        for i in range(ncols):
            _col_name = columns[i] if columns is not None else f"Date{i}"
            out_df[_col_name] = self._generate_dates(start=start, end=end)

        return out_df


if __name__ == "__main__":
    pass
