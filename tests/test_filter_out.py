from main import CsvHandler
import pytest
import argparse


def test_filter_out_multiple_values(capfd):
    '''
    Giving multiple comma seperated values in filter_out
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out="s_no,file_path", field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''line_no,issue_type,severity
42,buffer_overflow,HIGH
43,buffer_overflow,MED
40,buffer_overflow_1,HIGH
39,sqli,LOW
'''
    assert out == expected


def test_filter_out_single_values(capfd):
    '''
    Giving single value in filter_out
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out="severity", field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path,line_no,issue_type
1,repo1/core/utils/net.c,42,buffer_overflow
2,repo2/core/utils/net.c,43,buffer_overflow
3,repo3/core/utils/net1.c,40,buffer_overflow_1
4,eepo4/core/utils/net1.c,39,sqli
'''
    assert out == expected


def test_filter_out_single_invalid_values(capfd):
    '''
    Giving single invalid value in filter_out
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out="severity_1", field_order=None)
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.process()
    assert "Unknown columns in filter_out" in str(excinfo)

def test_filter_out_one_valid_one_invalid_values(capfd):
    '''
    Giving one valid and one invalid value in filter_out
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out="severity,s_no_1", field_order=None)
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.process()
    assert "Unknown columns in filter_out" in str(excinfo)
