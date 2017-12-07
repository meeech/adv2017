import math

def main(target):
    print('Target is %s' % target)
    if target == 1:
        return 0

    # shortcut relationship
    # MAX is sqrt -1, MIN is half that value
    # if float, result rounded UP must be ODD number. If EVEN number, then its in the top-right section

    sqrt = math.sqrt(target)
    if sqrt.is_integer():
        print('sqrt shortcut found...')
        return sqrt - 1


    # which quadrant
    print(sqrt)




assert(main(1) == 0)
assert(main(25) == 4)
assert(main(1024) == 31)
print(main(12) == 3)
print(main(23) == 2)
# main(265149)
