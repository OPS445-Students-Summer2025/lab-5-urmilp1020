#!/usr/bin/env python3

def add(number1, number2):
    """Add two numbers, return result or error string"""
    try:
        return int(number1) + int(number2)
    except (TypeError, ValueError):
        return 'error: could not add numbers'

def read_file(filename):
    """Read file and return lines or error string"""
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
