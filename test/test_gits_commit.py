import argparse
import os
import sys
import gits_commit
from mock import patch, Mock
sys.path.insert(1, os.getcwd())


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(m="dummy", amend=True))
@patch("subprocess.Popen", return_value="dummy")
def test_gits_commit_func_1(mock_var, mock_args):
    """
    Function to test gits_add, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_commit.gits_commit_func(mock_args)
    assert True == test_result, "success case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen", return_value="dummy")
def test_gits_commit_func_2(mock_var, mock_args):
    """
    Function to test gits_add, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_commit.gits_commit_func(mock_args)
    assert False == test_result, "Missing paramter"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(m="dummy", amend=False))
@patch("subprocess.Popen", return_value="dummy")
def test_gits_commit_func_3(mock_var, mock_args):
    """
    Function to test gits_add, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_commit.gits_commit_func(mock_args)
    assert True == test_result, "Amend is false"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(amend=False))
@patch("subprocess.Popen", return_value="dummy")
def test_gits_commit_func_4(mock_var, mock_args):
    """
    Function to test gits_add, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_commit.gits_commit_func(mock_args)
    assert False == test_result, "Empty commit message, amend is true"
