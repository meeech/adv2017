import itertools
import re
import sys
badchars = re.compile('(?:[A-Z\d])')

def has_anagram(pieces):
    for tup in itertools.combinations(pieces, 2):
        print(tup)
        a = list(tup[0])
        b = list(tup[1])
        a.sort()
        b.sort()
        if a == b:
            return True

    return False


def is_valid(_line):

    pieces = _line.split(' ')

    if len(pieces) == 1:
        return False

    if badchars.search(_line):
        return False

    if len(pieces) != len(set(pieces)):
        return False

    if has_anagram(pieces):
        return False

    return True


def main():
    count = 0
    for line in sys.stdin:
        if is_valid(line.replace('\n', '')):
            count = count + 1
        else:
            print(line)
    return count

print(is_valid('aa bb cc dd ee') == True)
print(is_valid('aa bb cc dd aa') == False)
print(is_valid('aa bb cc dd aaa') == True)
print(is_valid('aa Bb cc dd') == False)

print(main())
