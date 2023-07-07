from main import CsvHandler
import argparse


def test_sort_and_filter_in_multiple_values(capfd):
    '''
    Giving multiple comma seperated values in filter_in and single in sort_by
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="line_no", filter_in="line_no,file_path", filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''file_path,line_no
eepo4/core/utils/net1.c,39
repo3/core/utils/net1.c,40
repo1/core/utils/net.c,42
repo2/core/utils/net.c,43
'''
    assert out == expected

def test_sort_and_filter_in_single_value(capfd):
    '''
    Giving single value in filter_in and single in sort_by
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="line_no", filter_in="line_no", filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''line_no
39
40
42
43
'''
    assert out == expected

def test_ivalid_sort_and_filter_in_single_value(capfd):
    '''
    Giving single value in filter_in and single invalid value in sort_by
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="s_no", filter_in="line_no", filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''line_no
42
43
40
39
'''
    assert out == expected
