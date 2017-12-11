import sys

def main():
    in_maze = True
    lines = list(map(int, sys.stdin.read().splitlines()))
    current_offset = 0
    steps = 0

    while in_maze:

        to_move = lines[current_offset]
        lines[current_offset] = lines[current_offset] + 1

        current_offset = current_offset + to_move
        steps = steps + 1
        in_maze =  0 <= current_offset < len(lines)

main()
