import argparse
import os
import sys
from gits_unstage import unstage
from mock import patch, Mock
sys.path.insert(1, os.getcwd())


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(file_names=["test1", "test2"]))
@patch("subprocess.Popen")
def test_gits_stage(mock_var, mock_args):
    """
    Function to test gits stage, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = unstage(mock_args)
    assert True == test_result, "Success case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("gits_logging.gits_logger")
def test_gits_stage_sad_case(mock_err, mock_args):
    """
    Function to test gits unstage, failure case
    """
    mock_args = parse_args(mock_args)
    test_result = unstage(mock_args)
    assert False == test_result


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(file_names=[]))
@patch("subprocess.Popen")
def test_gits_unstage_happy_case_no_files(mock_var, mock_args):
    """
    Function to test gits stage, success case when no files are passed as argument
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = unstage(mock_args)
    assert True == test_result, "success case"
