import numpy

def plus_one(x):
    return x + 1

def test_method():
    assert plus_one(3) == 3 + 1, "test failed because " + str(plus_one(3)) + " is not equal to " + str(3 + 1)



