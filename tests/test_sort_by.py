from main import CsvHandler
import argparse


def test_severity_value_in_sort_by(capfd):
    '''
    Giving severity value in sort_by
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="severity", filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path,line_no,issue_type,severity
4,eepo4/core/utils/net1.c,39,sqli,LOW
2,repo2/core/utils/net.c,43,buffer_overflow,MED
1,repo1/core/utils/net.c,42,buffer_overflow,HIGH
3,repo3/core/utils/net1.c,40,buffer_overflow_1,HIGH
'''
    assert out == expected


def test_s_no_value_in_sort_by(capfd):
    '''
    Giving s_no value in sort_by
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="s_no", filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path,line_no,issue_type,severity
1,repo1/core/utils/net.c,42,buffer_overflow,HIGH
2,repo2/core/utils/net.c,43,buffer_overflow,MED
3,repo3/core/utils/net1.c,40,buffer_overflow_1,HIGH
4,eepo4/core/utils/net1.c,39,sqli,LOW
'''
    assert out == expected


def test_file_path_value_in_sort_by(capfd):
    '''
    Giving file_path value in sort_by
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="file_path", filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path,line_no,issue_type,severity
4,eepo4/core/utils/net1.c,39,sqli,LOW
1,repo1/core/utils/net.c,42,buffer_overflow,HIGH
2,repo2/core/utils/net.c,43,buffer_overflow,MED
3,repo3/core/utils/net1.c,40,buffer_overflow_1,HIGH
'''
    assert out == expected


def test_line_no_value_in_sort_by(capfd):
    '''
    Giving line_no value in sort_by
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="line_no", filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path,line_no,issue_type,severity
4,eepo4/core/utils/net1.c,39,sqli,LOW
3,repo3/core/utils/net1.c,40,buffer_overflow_1,HIGH
1,repo1/core/utils/net.c,42,buffer_overflow,HIGH
2,repo2/core/utils/net.c,43,buffer_overflow,MED
'''
    assert out == expected


def test_issue_type_value_in_sort_by(capfd):
    '''
    Giving issue_type value in sort_by
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="issue_type", filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path,line_no,issue_type,severity
1,repo1/core/utils/net.c,42,buffer_overflow,HIGH
2,repo2/core/utils/net.c,43,buffer_overflow,MED
3,repo3/core/utils/net1.c,40,buffer_overflow_1,HIGH
4,eepo4/core/utils/net1.c,39,sqli,LOW
'''
    assert out == expected



def test_invalid_value_in_sort_by(capfd):
    '''
    Giving invalid value in sort_by
    '''
    path = "tests/test_file_1.csv"
    args = argparse.Namespace(csv_file=path, sort_by="issue_type1", filter_in=None, filter_out=None, field_order=None)
    handler = CsvHandler(args)
    handler.process()
    out, error = capfd.readouterr()
    expected = '''s_no,file_path,line_no,issue_type,severity
1,repo1/core/utils/net.c,42,buffer_overflow,HIGH
2,repo2/core/utils/net.c,43,buffer_overflow,MED
3,repo3/core/utils/net1.c,40,buffer_overflow_1,HIGH
4,eepo4/core/utils/net1.c,39,sqli,LOW
'''
    assert out == expected
