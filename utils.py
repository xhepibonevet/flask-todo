import os

BASE_DIR = os.getcwd()


def read_file(f="done"):
    with open(f"{BASE_DIR}\\data\\{f}.txt", "r") as input_file:
        lines = [line.replace("\n", "") for line in input_file.readlines()]
    return lines

def write_file(new_lines, f="done"):
    all_lines = new_lines
    os.remove(f"{BASE_DIR}\\data\\{f}.txt")
    with open(f"{BASE_DIR}\\data\\{f}.txt", "w") as input_file:
        for line in all_lines:
            input_file.write(line + "\n")

def transfer_line(line_to_transfer):
    todo_lines = read_file(f="todo")
    done_lines = read_file(f="done")
    if line_to_transfer in todo_lines:
        todo_lines.remove(line_to_transfer)
        done_lines.append(line_to_transfer)
        write_file(todo_lines, f="todo")
        write_file(done_lines, f="done")
        print(todo_lines)
        print(done_lines)
    else:
        print("LINE IS NOT IN TODO")


def lines_to_dict(lines_list):
    return [{"title": line.split(":")[0], "description": line.split(":")[1]} for line in lines_list]
