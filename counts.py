def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "No characters"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("$%£@") == 0, "Special characters"
assert count_upper_case("Hi") == 1, "One upper case, one lower case"
assert count_upper_case("Hello") == 1, "One upper case, 4 lower case"
assert count_upper_case("Hello There") == 2, "Two capitalised words"
assert count_upper_case("Randy went to the store. He said, \"Hey Mr. Jones! How's it hanging?\"") == 6, "Sentence with 6 upper and special characters"

print("All tests passed")