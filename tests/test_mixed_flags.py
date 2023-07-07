from main import CsvHandler
import pytest
import argparse


def test_all_flags_with_valid(capfd):
    '''
    Giving valid values for all the fields
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="line_no", filter_in="file_path,severity,line_no", filter_out="line_no", field_order="severity,line_no,file_path")
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''severity,line_no,file_path
LOW,39,eepo4/core/utils/net1.c
HIGH,40,repo3/core/utils/net1.c
HIGH,42,repo1/core/utils/net.c
MED,43,repo2/core/utils/net.c
'''
    assert out == expected

def test_all_flags_with_valid_except_filter_out(capfd):
    '''
    Giving valid values for all the fields except filter_out
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="line_no", filter_in="file_path,severity,line_no", filter_out="line_no", field_order="severity,line_no,file_path")
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''severity,line_no,file_path
LOW,39,eepo4/core/utils/net1.c
HIGH,40,repo3/core/utils/net1.c
HIGH,42,repo1/core/utils/net.c
MED,43,repo2/core/utils/net.c
'''
    assert out == expected


def test_all_flags_with_valid_except_filter_out_with_invalid(capfd):
    '''
    Giving valid values for all the fields except filter_out with invalid value
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="line_no", filter_in="file_path,severity,line_no", filter_out="line_no_1", field_order="severity,line_no,file_path")
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.process()
    assert "Unknown columns in filter_out" in str(excinfo)


def test_sort_by_and_order(capfd):
    '''
    Giving valid sort_by and field order
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="line_no", filter_in=None, filter_out=None, field_order="severity,issue_type,file_path")
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''severity,issue_type,file_path,s_no,line_no
LOW,sqli,eepo4/core/utils/net1.c,4,39
HIGH,buffer_overflow_1,repo3/core/utils/net1.c,3,40
HIGH,buffer_overflow,repo1/core/utils/net.c,1,42
MED,buffer_overflow,repo2/core/utils/net.c,2,43
'''
    assert out == expected


def test_same_value_in_filter_out_and_order(capfd):
    '''
    Giving same column name in filter out and order
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out="issue_type", field_order="issue_type")
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path,line_no,severity
1,repo1/core/utils/net.c,42,HIGH
2,repo2/core/utils/net.c,43,MED
3,repo3/core/utils/net1.c,40,HIGH
4,eepo4/core/utils/net1.c,39,LOW
'''
    assert out == expected


def test_same_value_in_filter_in_and_order(capfd):
    '''
    Giving filtered column name using filter in and order
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in="s_no,file_path,line_no,severity", filter_out=None, field_order="issue_type")
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path,line_no,severity
1,repo1/core/utils/net.c,42,HIGH
2,repo2/core/utils/net.c,43,MED
3,repo3/core/utils/net1.c,40,HIGH
4,eepo4/core/utils/net1.c,39,LOW
'''
    assert out == expected
