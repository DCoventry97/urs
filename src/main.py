#!/usr/bin/python3
import sys

print(sys.argv)


def check_input(input_list):

    if input_list[1] == "-n" or input_list[1] == "--new":
        return 1

    elif input_list[1] == "-h" or input_list[1] == "--help" or input_list[1] == "help":
        return 2

    elif input_list[1] == "-r" or input_list[1] == "--rename":
        return 3

    elif input_list[1] == "-d" or input_list[1] == "--delete":
        return 4
