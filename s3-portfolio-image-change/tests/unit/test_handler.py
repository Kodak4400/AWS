import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__))  + '/../../change_function')

import pytest
import app

def test_lambda_handler():
    assert app.lambda_handler('test', "") == {'hellow world'}