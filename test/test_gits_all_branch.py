import os
import sys
import argparse
import gits_all_branch
from mock import patch, Mock
sys.path.insert(1, os.getcwd())

def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)

@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_all_branch_happy(mock_var, mock_args):
    """
    Gits all-branch Success Case
    """
    mocked_obj = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_obj.configure_mock(**attrs)
    mock_var.return_value = mocked_obj
    mock_args = parse_args(mock_args)
    test_result = gits_all_branch.gits_all_branch_func(mock_args)
    assert True == test_result
