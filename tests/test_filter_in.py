from main import CsvHandler
import pytest
import argparse


def test_filter_in_multiple_values(capfd):
    '''
    Giving multiple comma seperated values in filter_in
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in="s_no,file_path", filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path
1,repo1/core/utils/net.c
2,repo2/core/utils/net.c
3,repo3/core/utils/net1.c
4,eepo4/core/utils/net1.c
'''
    assert out == expected

def test_filter_in_single_value(capfd):
    '''
    Giving single in filter_in
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in="s_no", filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no
1
2
3
4
'''
    assert out == expected


def test_filter_in_invalid_single_value(capfd):
    '''
    Giving invalid in filter_in
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in="s_no1", filter_out=None, field_order=None)
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.process()
    assert "Unknown columns in filter_in" in str(excinfo)

def test_filter_in_one_invalid_one_valid_value(capfd):
    '''
    Giving one invalid and one valid value in filter_in
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in="s_no,file_path1", filter_out=None, field_order=None)
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.process()
    assert "Unknown columns in filter_in" in str(excinfo)


