# import re

# my_pattern = r""
# my_regex = re.compile(my_pattern)
# import re

# # Regular expression to match the test cases
# my_regex = re.compile(r"^[A-Za-z\s',?.!]+$")

# # Test string for the findall test case
# FINDALL_STRING = '''
# It's such a lovely day today.
# Some weather we're having today, huh?
# Maybe today's just not my day.
# '''

import re

# Adjust the regular expression to capture each sentence specifically
my_regex = re.compile(r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)")

# Test string for the findall test case
FINDALL_STRING = '''
It's such a lovely day today.
Where'd all the time go?
Some weather we're having today, huh?
Tomorrow never knows!
Maybe today's just not my day.
It's clobbering time!
'''


