from main import CsvHandler
import pytest
import argparse



def test_field_order_multiple_values(capfd):
    '''
    Giving multiple comma seperated values in field_order
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out=None, field_order="severity,s_no,file_path")
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''severity,s_no,file_path,line_no,issue_type
HIGH,1,repo1/core/utils/net.c,42,buffer_overflow
MED,2,repo2/core/utils/net.c,43,buffer_overflow
HIGH,3,repo3/core/utils/net1.c,40,buffer_overflow_1
LOW,4,eepo4/core/utils/net1.c,39,sqli
'''
    assert out == expected


def test_field_order_multiple_values_2(capfd):
    '''
    Giving multiple comma seperated values in field_order
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out=None, field_order="severity,s_no,line_no,file_path")
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''severity,s_no,line_no,file_path,issue_type
HIGH,1,42,repo1/core/utils/net.c,buffer_overflow
MED,2,43,repo2/core/utils/net.c,buffer_overflow
HIGH,3,40,repo3/core/utils/net1.c,buffer_overflow_1
LOW,4,39,eepo4/core/utils/net1.c,sqli
'''
    assert out == expected


def test_field_order__single_value(capfd):
    '''
    Giving single values in field_order
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out=None, field_order="severity")
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''severity,s_no,file_path,line_no,issue_type
HIGH,1,repo1/core/utils/net.c,42,buffer_overflow
MED,2,repo2/core/utils/net.c,43,buffer_overflow
HIGH,3,repo3/core/utils/net1.c,40,buffer_overflow_1
LOW,4,eepo4/core/utils/net1.c,39,sqli
'''
    assert out == expected

def test_field_order_invalid_single_value():
    '''
    Giving single invalid value in field_order
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out=None, field_order="severity_2")
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.process()
    assert "Unknown columns in field_order" in str(excinfo)

def test_field_order_invalid_single_value():
    '''
    Giving single invalid value and one valid value in field_order
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by=None, filter_in=None, filter_out=None, field_order="severity,SS_No")
    handler = CsvHandler(args)
    with pytest.raises(Exception) as excinfo:
        handler.process()
    assert "Unknown columns in field_order" in str(excinfo)
