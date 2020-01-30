#!/usr/bin/env python3

from inspect import currentframe
from pprint import pformat
from sys import stderr

BOLD_BLUE = "\033[1;34m"
BOLD_CYAN = "\033[1;36m"
BOLD_PURPLE = "\033[1;35m"
BOLD = "\033[1m"
BOLD_UNDERLINE = "\033[1;4m"
CLOSE = "\033[0m"

CAPACITY = 10
VALUE = 0


def exit_with_error(func_name, line_number):
    print("<{}{}{}>.{}{}{}() @{}line {}{}: {}Exit{}".format(
        BOLD,
        __name__,
        CLOSE,
        BOLD,
        func_name,
        CLOSE,
        BOLD_UNDERLINE,
        line_number,
        CLOSE,
        BOLD_PURPLE,
        CLOSE,
        file=stderr,
    ))
    exit(1)


def enqueue(queue, value):
    if queue["remaining_cap"] < 1:
        return False
    queue["memory"][queue["end"]] = value
    queue["end"] = (queue["end"] + 1) % CAPACITY
    queue["remaining_cap"] -= 1
    return True


def dequeue(queue):
    if CAPACITY <= queue["remaining_cap"]:
        return None
    index = queue["start"]
    value = queue["memory"][index]
    queue["memory"][index] = None
    queue["start"] = (queue["start"] + 1) % CAPACITY
    queue["remaining_cap"] += 1
    return value


def do_enqueue(queue, n):
    print("\n{}enqueue{}(..., {}{}{}) @ {}end: {}{}\n".format(
        BOLD,
        CLOSE,
        BOLD_BLUE,
        n,
        CLOSE,
        BOLD_UNDERLINE,
        queue["end"],
        CLOSE,
    ))
    for _ in range(n):
        global VALUE
        print("    {}".format(VALUE))
        if not enqueue(queue, VALUE):
            exit_with_error(
                currentframe().f_code.co_name,
                currentframe().f_lineno - 3,
            )
        else:
            VALUE += 1
    print("\n", pformat(queue), sep="")


def do_dequeue(queue, n):
    print("\n{}dequeue{}(..., {}{}{}) @ {}start: {}{}\n".format(
        BOLD,
        CLOSE,
        BOLD_CYAN,
        n,
        CLOSE,
        BOLD_UNDERLINE,
        queue["start"],
        CLOSE,
    ))
    for _ in range(n):
        value = dequeue(queue)
        if value is None:
            exit_with_error(
                currentframe().f_code.co_name,
                currentframe().f_lineno - 3,
            )
        else:
            print("    {}".format(value))
    print("\n", pformat(queue), sep="")


def main():
    queue = {
        "memory": [None] * CAPACITY,
        "start": 0,
        "end": 0,
        "remaining_cap": CAPACITY,
    }
    do_enqueue(queue, 8)
    do_dequeue(queue, 3)
    do_enqueue(queue, 5)
    do_dequeue(queue, 9)
    do_enqueue(queue, 3)
    do_dequeue(queue, 1)
    do_enqueue(queue, 7)
    do_dequeue(queue, 1)


if __name__ == "__main__":
    main()
