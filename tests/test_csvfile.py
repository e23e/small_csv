from main import CsvHandler
import pytest
import argparse


def test_invalid_ext():
    '''
    Giving file with invalid ext in the csv_file arg
    '''
    path = "invalid.jpg"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.validate()
    assert "File Extension is not supported" in str(excinfo)


def test_valid_ext():
    '''
    Giving valid file with valid ext in the csv_file arg
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    assert handler.validate() == None


def test_invalid_path():
    '''
    Giving invalid path
    '''
    path = "test/file_2.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.validate()
    assert "File not found, please check the file path!" in str(excinfo)

def test_empty_file():
    '''
    Giving empty file
    '''
    path = "tests/test_file_empty.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.validate()
    assert "Empty csv file given" in str(excinfo)


