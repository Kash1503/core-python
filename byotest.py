# Check to see if two values are equal
def test_are_equal(expected, actual):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
# Check to see if two values are not equal
def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
# Check to see if item is in collection
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
# check to see if item is not in the collection
def test_not_in(collection, item):
    assert item not in collection, "{0} contains {1}, which is unexpected".format(collection, item)
    
# test to see if value is between an upper and lower limit, inclusively
def test_between(upper, number, lower):
    assert number < upper, "{0} is larger than {1}, the upper limit".format(number, upper)
    assert number > lower, "{0} is smaller than {1}, the lower limit".format(number, lower)