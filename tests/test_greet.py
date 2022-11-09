from lib.greet import greet

def test_greet_is_hello_dan():
    result = greet('Dan')
    assert result=="Hello, Dan!"

