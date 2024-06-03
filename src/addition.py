# app.py
# this is good test
def add(a, b):
    return a + b
#test starts here
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
