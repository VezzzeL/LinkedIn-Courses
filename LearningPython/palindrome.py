import re

show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    teststr_lower = re.sub('[^0-9a-zA-Z]+', '', teststr.lower())
    return teststr_lower == teststr_lower[::-1]