#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    if length == 1:
        print([0])
        return
        

    fib_seq = [0, 1]
# common approach to fib sequence: iterative approach uses a loop
    while len(fib_seq) < length:
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)

    print(fib_seq)
