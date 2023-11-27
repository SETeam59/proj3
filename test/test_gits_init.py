import argparse
import sys
import os
import shutil

sys.path.insert(1, os.getcwd())

from gits_init import gits_init_func
from mock import patch


def remove_file(file):
    try:
        shutil.rmtree(file)
    except:
        os.remove(file)


def delete_non_pys(path):
    files = os.listdir(path)
    for file in files:
        if "py" not in file:
            remove_file(file)
        
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(bare=None, amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_deafult(mock_var1, mock_args):
    """
    Function to test gits init default case without parameters
    """
    test_result = gits_init_func(mock_args)
    delete_non_pys(".")
    assert test_result == True

@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(bare=True, amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_with_bare(mock_var1, mock_args):
    """
    Function to test gits init with --bare parameter
    """
    test_result = gits_init_func(mock_args)
    delete_non_pys(".")
    assert test_result == True