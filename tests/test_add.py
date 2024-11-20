from src.app import add

def test_add():
    assert add(4, 5) == 9

def test_fail_add():
    assert add(4, 5) == 10
