from lib.report_length import *

def test_length():
    result = report_length("Example String")
    assert result == "This string was 14 characters long."