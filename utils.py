import os

BASE_DIR = os.getcwd()


def read_file(f="done"):
    with open(f"{BASE_DIR}//data//{f}.txt", "r") as input_file:
        lines = [line.replace("\n", "") for line in input_file.readlines()]
    return lines

def write_file(new_lines, f="done"):
    lines = read_file(f)
    all_lines = lines + new_lines
    with open(f"{BASE_DIR}//data//{f}.txt", "w") as input_file:
        for line in all_lines:
            input_file.write(line + "\n")
