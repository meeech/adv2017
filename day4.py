import sys
import re
count = 0
badchars = re.compile('(?:[A-Z\d])')

def is_valid(_line):

    pieces = _line.split(' ')

    if len(pieces) == 1:
        return False

    if badchars.search(_line):
        return False

    return len(pieces) == len(set(pieces))

for line in sys.stdin:
    if is_valid(line.replace('\n', '')):
        count = count + 1
    else:
        print(line)

print(is_valid('aa bb cc dd ee') == True)
print(is_valid('aa bb cc dd aa') == False)
print(is_valid('aa bb cc dd aaa') == True)
print(is_valid('aa Bb cc dd') == False)

print(count)
