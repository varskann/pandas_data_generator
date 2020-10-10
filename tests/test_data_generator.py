"""
Randen: Random DataFrame Generator
    Testcases for randen
TODO: Add testcases for provided column names
TODO: Test for nullratio funcionality
"""
__author__ = "Kanishk Varshney"
__date__ = "05-10-2020"
__appname__ = "randen"

from datetime import datetime
from pandas.api.types import is_datetime64_any_dtype as is_datetime

from randen import DataFrameGenerator

def test_get_integer_dataframe():
    """
    Test Integer dataframe generation
        - Test the returned dataframe shape
        - Test the auto-generated column names
        - Test the datatypes
    Returns:

    """
    dfg = DataFrameGenerator()
    df = dfg.get_integer_dataframe(10, 5)
    assert df.shape == (10, 5), "Wrong size dataframe generated"
    assert list(df.columns) == ["Integer0", "Integer1", "Integer2", "Integer3", "Integer4"], "Wrong column names"
    assert df.dtypes.values.all() == int, "Wrong data types"


def test_get_float_dataframe():
    """
    Test Float dataframe generation
        - Test the returned dataframe shape
        - Test the auto-generated column names
        - Test the datatypes
    Returns:

    """
    dfg = DataFrameGenerator()
    df = dfg.get_float_dataframe(10, 5)
    assert df.shape == (10, 5), "Wrong size dataframe generated"
    assert list(df.columns) == ["Float0", "Float1", "Float2", "Float3", "Float4"], "Wrong column names"
    assert df.dtypes.values.all() == float, "Wrong data types"


def test_get_bool_dataframe():
    """
    Test Boolean dataframe generation
        - Test the returned dataframe shape
        - Test the auto-generated column names
        - Test the datatypes
    Returns:

    """
    dfg = DataFrameGenerator()
    df = dfg.get_boolean_dataframe(10, 5)
    assert df.shape == (10, 5), "Wrong size dataframe generated"
    assert list(df.columns) == ["Bool0", "Bool1", "Bool2", "Bool3", "Bool4"], "Wrong column names"
    assert df.dtypes.values.all() == bool, "Wrong data types"


def test_get_char_dataframe():
    """
    Test Bytes/Char dataframe generation
        - Test the returned dataframe shape
        - Test the auto-generated column names
        - Test the datatypes
    Returns:

    """
    dfg = DataFrameGenerator()
    df = dfg.get_char_dataframe(10, 5)
    assert df.shape == (10, 5), "Wrong size dataframe generated"
    assert list(df.columns) == ["Char0", "Char1", "Char2", "Char3", "Char4"], "Wrong column names"
    assert df.dtypes.values.all() == object, "Wrong data types"


def test_get_string_dataframe():
    """
    Test String dataframe generation
        - Test the returned dataframe shape
        - Test the auto-generated column names
        - Test the datatypes
    Returns:

    """
    dfg = DataFrameGenerator()
    df = dfg.get_string_dataframe(10, 5)
    assert df.shape == (10, 5), "Wrong size dataframe generated"
    assert list(df.columns) == ["Str0", "Str1", "Str2", "Str3", "Str4"], "Wrong column names"
    assert df.dtypes.values.all() == object, "Wrong data types"


def test_get_date_dataframe():
    """
    Test Datetime dataframe generation
        - Test the returned dataframe shape
        - Test the auto-generated column names
        - Test the datatypes
    Returns:

    """
    dfg = DataFrameGenerator()
    df = dfg.get_dates_dataframe(10, 5)
    assert df.shape == (10, 5), "Wrong size dataframe generated"
    assert list(df.columns) == ["Date0", "Date1", "Date2", "Date3", "Date4"], "Wrong column names"
    assert is_datetime(df.dtypes.values.all()), "Wrong data types"


def test_get_dataframe():
    """
    Test Generic dataframe generation
        - Test the returned dataframe shape
        - Test the auto-generated column names
        - Test the datatypes
    Returns:

    """
    dfg = DataFrameGenerator()
    df = dfg.get_dataframe(10, ctypes=[str, bytes, int, float, bool, datetime])
    assert df.shape == (10, 6), "Wrong size dataframe generated"
    assert list(df.columns) == ["Str0", "Bytes1", "Int2", "Float3", "Bool4", "Datetime5"], "Wrong column names"
