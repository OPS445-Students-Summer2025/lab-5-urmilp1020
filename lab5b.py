#!/usr/bin/env python3

def read_file_string(file_name):
    """Read file and return as string"""
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """Read file and return as list of lines without newlines"""
    with open(file_name, 'r') as f:
        return [line.rstrip('\n') for line in f]

def append_file_string(file_name, string_of_lines):
    """Append string to file"""
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Write list to file with newlines"""
    with open(file_name, 'w') as f:
        f.write('\n'.join(list_of_lines) + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Copy file with line numbers added"""
    with open(file_name_read, 'r') as f_read:
        lines = f_read.readlines()
    
    with open(file_name_write, 'w') as f_write:
        for i, line in enumerate(lines, 1):
            f_write.write(f"{i}:{line}")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
