import logging
from sys import argv
from os import path
from aocHelpers import inputs
from aocHelpers.decorators import timer, print_result
from aocHelpers.init import init
import re


@timer
@print_result
def exercise1(arr):
	return sum([int(i.group()) for i in re.finditer(r'-?\d+', arr)])


@timer
@print_result
def exercise2(arr):
	pass

def main(args=None):
	arr = init(path.dirname(__file__), inputs.read_to_str_arr, args)
	exercise1("".join(arr))
	exercise2(arr.copy())

if __name__ == "__main__":
	main(argv[1:])
