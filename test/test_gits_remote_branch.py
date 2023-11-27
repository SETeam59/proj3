import os
import sys
import argparse
import gits_remote_branch
sys.path.insert(1, os.getcwd())
from mock import patch, Mock

def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)

@patch("argparse.ArgumentParser.parse_args",return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_remote_branch_happy(mock_var, mock_args):
    """
    Git remote-branch Success Case  
    """
    mocked_obj = Mock()
    attrs = {'communicate.return_value': ('output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_obj.configure_mock(**attrs)
    mock_var.return_value = mocked_obj
    mock_args = parse_args(mock_args)
    test_result = gits_remote_branch.gits_remote_branch_func(mock_args)
    assert True == test_result
