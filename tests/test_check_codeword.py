from lib.check_codeword import *

def test_codeword_is_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_codeword_is_not_horse():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_codeword_wrong():
    result = check_codeword("dsgdsag")
    assert result == "WRONG!"

