#!/usr/bin/env python3

'''
Warning: 

There is no guarantee that this file makes sense out
of context.
'''


import timeit
import dis

def comp():
    a = [i**2 for i in range(10000)]

# def loops():
#     a = []
#     for i in range(10000):
#         a.append(i**2)


def map_example_comp():
    add_2 = [(num + 2) for num in range(1000)]

def map_example():
    add_2 = list(map(lambda x: x+2, range(1000)))
    # print(type(add_2))

list_comp_times = timeit.timeit(map_example_comp, number = 10000)
# print(list_comp_times)

list_comp_times = timeit.timeit(map_example, number = 10000)
# print(list_comp_times)


def square_nums():
    squares = []
    for num in range(15):
        squares.append(num**2)
    print(squares)

# print list of first 15 square numbers
def square_nums_comps():
    # square_nums = [(computation) for num in (iterable)]
    square_nums = [num**2 for num in range(15)]
    print(square_nums)

# print even of the first 15 nums
def square_nums_conditional():
    square_nums = [num**2 for num in range(15) if num % 2 == 0 ]
    print(square_nums)
    # # square_nums = [(computation) for num in (iterable) *if (expr)*]

square_nums_conditional()

words = ["foo", "bar", "alpha", "gamma"]



# reduce -> import functools


# [1,4,9,...]


def loops():
    a = []
    for i in range(1,1000):
        a.append(i**2)
    print(a)


# loops()

# print list of first 15 square numbers
def square_nums_comps():
    
    # [(expression) for (num) in (iterable)]
    square_nums = [num**2 for num in range(1,1000)]
    print(square_nums)

def square_nums_map():
    nums = list(map(lambda x: x**2, range(1,1000)))
    print(nums)
    # assert(a == b) or pytest unit test
    # reduce - > functools module
    # alternatively, create a generator

# comp = timeit.timeit(square_nums_comps, number = 1000)
# map = timeit.timeit(square_nums_map, number = 1000)
# append_for = timeit.timeit(loops, number = 1000)


