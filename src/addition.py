# app.py
def add(a, b):
    return a + b

#test case
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
