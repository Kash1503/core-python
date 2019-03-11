# Check to see if two values are equal
def test_are_equal(expected, actual):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
# Check to see if two values are not equal
def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
# Check to see if item is in collection
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)