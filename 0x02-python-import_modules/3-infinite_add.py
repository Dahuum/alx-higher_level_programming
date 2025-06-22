#!/usr/bin/python3

if __name__ == "__main__":
    """print addition of all arguments."""
    import sys

    sum = 0
    ac = len(sys.argv) - 1
    for i in range(1, ac + 1):
        sum += int(sys.argv[i])
    print("{}".format(sum))
