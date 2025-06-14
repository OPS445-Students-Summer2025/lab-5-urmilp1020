#!/usr/bin/env python3


def read_file_string(file_name):
    """Read file and return as string"""
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """Read file and return as list of lines without newlines"""
    with open(file_name, 'r') as f:
        return [line.rstrip('\n') for line in f]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
