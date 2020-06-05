import command_maker as cm
import os.path
import timeit
import types
import functools
import copy
import random


class Pretty(list):
    def __str__(self):
        result = [str(i) for i in self]
        return "\n".join(result)


class Handler(cm.Controller):
    def __init__(self):
        self.create_modes = {}
        self.traverse_modes = {}
        self.sort_modes = {}
        super().__init__()


handler = Handler()
handler.commands = cm.controller.commands


@cm.add_to_switch(switch=handler.create_modes)
def matrix(data):
    """Adjacency matrix"""
    data = Pretty(data)
    return data


@cm.add_to_switch(switch=handler.create_modes)
def table(data):
    """Adjacency list"""
    result = []
    for i in range(len(data)):
        result.append([])
        for j in range(len(data)):
            if data[i][j] == 1:
                result[i].append(j)
    data = Pretty(result)
    return data


@cm.add_to_switch(switch=handler.create_modes)
def lists(data):
    """List of edges"""
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 1:
                result.append((i,j))
    data = Pretty(result)
    return data


@cm.add_to_switch(switch=handler.commands)
@cm.correctness
def create(size: int) -> str:
    """
    Creates chosen representation [type] of the graph.
    :param size:
    :param type:
    :return:
    """
    data = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size - 1):
        for j in range(i + 1, size):
            data[i][j] = 1
    for name in handler.create_modes:
        result = handler.create_modes[name](data)
        cm.pklwrite(result, f"{name}.pkl")
    return "Graph generated successfully."


@cm.add_to_switch(switch=handler.commands)
def gen_from_txt() -> str:
    """
    Analyzes the input.txt file and generates graph representation from it.
    :return:
    """
    with open("input.txt", 'r') as origin:
        if (line := origin.readline().strip().split()) == []:
            return "input.txt file doesn't contain adjacency matrix (0)."
        dim = len(line)
        data = [[] for _ in range(dim)]
        counter = 0
        for charray in line:
            if charray == '1':
                data[counter].append(1)
            elif charray == '0':
                data[counter].append(0)
            else:
                return "input.txt file doesn't contain adjacency matrix (1)."
        counter += 1
        while counter < dim:
            if (line := origin.readline().strip().split()) == []:
                return "input.txt file doesn't contain adjacency matrix (2)."
            for charray in line:
                if charray == '1':
                    data[counter].append(1)
                elif charray == '0':
                    data[counter].append(0)
                else:
                    return "input.txt file doesn't contain adjacency matrix (3)."
            counter += 1
        else:
            if (line := origin.readline().strip().split()) != []:
                return "input.txt file doesn't contain adjacency matrix (4)."
        for name in handler.create_modes:
            result = handler.create_modes[name](data)
            cm.pklwrite(result, f"{name}.pkl")
        return "Graph generated successfully."



@cm.add_to_switch(switch=handler.commands, name="print")
@cm.availability(switch=handler.create_modes, name="representation types")
@cm.correctness
def new_print(type: str) -> str:
    """
    Prints the graph representation stored in [type].pkl file.
    :param type:
    :return:
    """
    if os.path.isfile(f"{type}.pkl"):
        return cm.pklread(f"{type}.pkl")
    else:
        return f"File {type}.pkl doesn't exist, generate data first."


def dfs_sort_decorator(func: types.FunctionType):
    """
    Joins the sort request with the desired algorythm to perform topological sorting
    :param func:
    :param data:
    :return:
    """
    @functools.wraps(func)
    def dfs_sort_wrapper(data: list):
        if isinstance(data[0], tuple):
            length = 0
            for i, j in data:
                length = max(length, max(i, j))
            check_list = [0 for _ in range(length + 1)]
        else:
            check_list = [0 for _ in range(len(data))]
        yield from func(data, 0, check_list)
        yield 2, -1, 0
        for i in range(1, len(check_list)):
            if check_list[i] == 0:
                yield from func(data, i, check_list)
                yield 2, -1, i

    return dfs_sort_wrapper


@cm.add_to_switch(switch=handler.sort_modes)
@dfs_sort_decorator
@cm.add_to_switch(switch=handler.traverse_modes)
def dfs_matrix(data: list, start: int = 0, check_list: list = []):
    """dfs - Adjacency matrix"""
    yield 0, -1, start
    if check_list == []:
        check_list = [0 for _ in data]
    path = [start]
    check_list[start] = 1
    j = 0
    while True:
        if j >= len(data):
            check_list[path[-1]] = 2
            if len(path) == 1:
                return
            else:
                yield 2, path[-2], path[-1]
                j = path.pop() + 1
                continue
        if check_list[j] != 2 and data[path[-1]][j] == 1:
            yield check_list[j], path[-1], j
            path.append(j)
            check_list[j] = 1
            j = 0
        else:
            j += 1


@cm.add_to_switch(switch=handler.sort_modes)
@dfs_sort_decorator
@cm.add_to_switch(switch=handler.traverse_modes)
def dfs_table(data: list, start: int = 0, check_list: list = []):
    """dfs - Adjacency list"""
    yield 0, -1, start
    if check_list == []:
        check_list = [0 for _ in data]
    check_list[start] = 1
    path = [start]
    j = 0
    while True:
        if j >= len(data[path[-1]]):
            check_list[path[-1]] = 2
            if len(path) == 1:
                return
            else:
                yield 2, path[-2], path[-1]
                path.pop()
                j = 0
                continue
        if check_list[data[path[-1]][j]] != 2:
            yield check_list[data[path[-1]][j]], path[-1], data[path[-1]][j]
            check_list[data[path[-1]][j]] = 1
            path.append(data[path[-1]][j])
            j = 0
        else:
            j += 1

@cm.add_to_switch(switch=handler.sort_modes)
@dfs_sort_decorator
@cm.add_to_switch(switch=handler.traverse_modes)
def dfs_list(data: list, start: int = 0, check_list: list = []):
    """dfs - List of edges"""
    if check_list == []:
        length= 0
        for i, j in data:
            length = max(length, max(i, j))
        check_list = [0 for _ in range(length + 1)]
    yield 0, -1, start
    path = [start]
    j = 0
    while True:
        if j >= len(data):
            check_list[path[-1]] = 2
            if len(path) == 1:
                return
            else:
                yield 2, path[-2], path[-1]
                path.pop()
                j = 0
                continue
        if data[j][0] == path[-1] and check_list[data[j][1]] != 2:
            yield check_list[data[j][1]], path[-1], data[j][1]
            check_list[data[j][1]] = 1
            path.append(data[j][1])
            j = 0
            continue
        j += 1


@cm.add_to_switch(switch=handler.sort_modes, name="bfs_matrix")
def bfs_matrix_sort(data:list):
    """bfs - Adjacency matrix"""
    incoming = []
    queue = []
    for i in range(len(data)):
        incoming.append(0)
        for j in range(len(data)):
            if data[j][i] == 1:
                incoming[i] += 1
        if incoming[i] == 0:
            queue.insert(0, i)
    while queue:
        yield queue[0]
        for i in range(len(data) - 1, -1, -1):
            if data[queue[0]][i] == 1:
                data[queue[0]][i] = 0
                incoming[i] -= 1
                if incoming[i] == 0:
                    queue.append(i)
        del queue[0]
    for i in range(len(data)):
        if incoming[i] != 0:
            yield -1


@cm.add_to_switch(switch=handler.sort_modes, name="bfs_table")
def bfs_table_sort(data: list):
    """bfs - Adjacency list"""
    incoming = [0 for _ in range(len(data))]
    queue = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            incoming[data[i][j]] += 1
    for i in range(len(data) - 1, -1, -1):
        if incoming[i] == 0:
            queue.append(i)
    while queue:
        yield queue[0]
        for i in range(len(data[queue[0]]) - 1, -1, -1):
            incoming[data[queue[0]][i]] -= 1
            if incoming[data[queue[0]][i]] == 0:
                queue.append(data[queue[0]][i])
            del data[queue[0]][i]
        del queue[0]
    for i in range(len(data)):
        if incoming[i] != 0:
            yield -1


@cm.add_to_switch(switch=handler.sort_modes, name="bfs_list")
def bfs_list_sort(data: list):
    """bfs - List of edges"""
    length = 0
    for i, j in data:
        length = max(length, max(i, j))
    incoming = [0 for _ in range(length + 1)]
    queue = []
    for i in range(len(data)):
        incoming[data[i][1]] += 1
    for i in range(length, -1, -1):
        if incoming[i] == 0:
            queue.append(i)
    while queue:
        yield queue[0]
        for i in range(len(data) - 1, -1, -1):
            if data[i][0] == queue[0]:
                incoming[data[i][1]] -= 1
                if incoming[data[i][1]] == 0:
                    queue.append(data[i][1])
                del data[i]
        del queue[0]
    for i in range(len(data)):
        if incoming[i] != 0:
            yield -1


@cm.add_to_switch(switch=handler.traverse_modes)
def bfs_matrix(data: list):
    """bfs - Adjacency matrix"""
    yield 0
    check_list = [0 for _ in data]
    queue = [0]
    check_list[0] = 1
    while queue:
        for i in range(len(data)):
            if check_list[i] == 0 and data[queue[0]][i] == 1:
                yield i
                check_list[i] = 1
                queue.append(i)
        del queue[0]


@cm.add_to_switch(switch=handler.traverse_modes)
def bfs_table(data: list):
    """bfs - Adjacency list"""
    yield 0
    check_list = [0 for _ in data]
    queue = [0]
    check_list[0] = 1
    while queue:
        for i in range(len(data[queue[0]])):
            if check_list[data[queue[0]][i]] == 0:
                yield data[queue[0]][i]
                check_list[data[queue[0]][i]] = 1
                queue.append(data[queue[0]][i])
        del queue[0]


@cm.add_to_switch(switch=handler.traverse_modes)
def bfs_list(data: list):
    """bfs - List of edges"""
    yield 0
    length = 0
    for i, j in data:
        length = max(length, max(i, j))
    check_list = [0 for _ in range(length + 1)]
    queue = [0]
    check_list[0] = 1
    while queue:
        for pair in data:
            if pair[0] == queue[0] and check_list[pair[1]] == 0:
                yield pair[1]
                check_list[pair[1]] = 1
                queue.append(pair[1])
        del queue[0]


@cm.add_to_switch(switch=handler.commands)
@cm.availability(switch=handler.traverse_modes, name="traversal algorythms")
@cm.correctness
def traverse(type: str) -> str:
    """
    Prints the traversal road based on the chosen [type] algorythm
    :param type:
    :return:
    """
    if (func := handler.traverse_modes.get(type)) is None:
        return f"{type} is not an available traversal algorythm."
    if os.path.isfile(f"{type[4::]}.pkl"):
        data = cm.pklread(f"{type[4::]}.pkl")
        result = ""
        if type[:3:] == "dfs":
            for i, j, k in func(data):
                if j == -1:
                    result += f"  -> {k}\n"
                elif i == 2:
                    result += f"{j} <- {k}\n"
                elif i == 0:
                    result += f"{j} -> {k}\n"
        else:
            for i in func(data):
                result += f" {i}"
        return result
    else:
        return f"File {type[4::]}.pkl doesn't exist, generate data first."


@cm.add_to_switch(switch=handler.commands)
@cm.availability(switch=handler.sort_modes, name="sorting algorythms")
@cm.correctness
def sort(type: str) -> str:
    """
    Performs a topological sort on a graph using the chosen [type] algorythm
    :param type:
    :return:
    """
    if (func := handler.sort_modes.get(type)) is None:
        return f"{type} is not an available traversal algorythm."
    if os.path.isfile(f"{type[4::]}.pkl"):
        data = cm.pklread(f"{type[4::]}.pkl")
        result = ""
        sorted = []
        if type[:3:] == "dfs":
            for i, j, k in func(data):
                if j == -1 and i == 0:
                    result += f"         -> {k} - white\n"
                elif j == -1 and i == 2:
                    result += f"         <- {k} - green\n"
                    sorted.insert(0, k)
                elif i == 0:
                    result += f"{j} - gray -> {k} - white\n"
                elif i == 2:
                    result += f"{j} - gray <- {k} - green\n"
                    sorted.insert(0, k)
                elif i == 1:
                    result += f"{j} - gray -> {k} - gray\nGraph contains a cycle\n"
                    break
            result += f"Result:\n{sorted}\n"
        else:
            for i in func(data):
                if i == -1:
                    result += "Graph contains a cycle\n"
                    break
                sorted.append(i)
            result += f"Result:\n{sorted}\n"
        return str(result)
    else:
        return f"File {type[4::]}.pkl doesn't exist, generate data first."


def first_second_third(data: list, degrees: list, check_list: list, size: int):
    while True:
        copy = list(check_list)
        if (first := draw_first(degrees, copy, size)) is None:
            return None, None, None
        second, third = second_and_third(data, degrees, copy, size, first)
        if second is None:
            check_list.remove(first)
        else:
            return first, second, third


def draw_first(degrees: list, check_list: list, size: int):
    first = min(check_list, key=lambda key: degrees[key])
    while degrees[first] == size:
        check_list.remove(first)
        if not check_list:
            return None
        first = min(check_list, key=lambda key: degrees[key])
    check_list.remove(first)
    if not check_list:
        return None
    return first


def draw_second(data: list, degrees: list, check_list: list, size: int, first: int):
    second = min(check_list, key=lambda key: degrees[key])
    while degrees[second] == size or data[first][second] == 1:
        check_list.remove(second)
        if not check_list:
            return None
        second = min(check_list, key=lambda key: degrees[key])
    check_list.remove(second)
    if not check_list:
        return None
    return second


def draw_third(data: list, degrees: list, check_list: list, size: int, first: int, second: int):
    third = min(check_list, key=lambda key: degrees[key])
    while degrees[third] == size or data[third][first] == 1 or data[second][third] == 1:
        check_list.remove(third)
        if not check_list:
            return None
        third = min(check_list, key=lambda key: degrees[key])
    check_list.remove(third)
    return third


def second_and_third(data: list, degrees: list, check_list: list, size: int, first: int):
    while True:
        if (second := draw_second(data, degrees, check_list, size, first)) is None:
            return None, None
        copy = list(check_list)
        if (third := draw_third(data, degrees, copy, size, first, second)) is not None:
            return second, third


def join(data: list, degrees: list, old: int, new: int):
    data[old][new], data[new][old] = 1, 1
    degrees[old] += 1
    degrees[new] += 1
    return new


@cm.add_to_switch(switch=handler.commands)
@cm.correctness
def create_hamilton(size: int, density: int):
    """
    Creates a directed graph
    :param size:
    :param denisty:
    :return:
    """
    data = [[0 for _ in range(size)] for _ in range(size)]
    degrees = [0 for _ in range(size)]
    check_list = [i for i in range(size)]
    start = random.choice(check_list)
    check_list.remove(start)
    old = start
    new = 0
    for _ in range(size - 1):
        new = random.choice(check_list)
        check_list.remove(new)
        old = join(data, degrees, old, new)
    else:
        join(data, degrees, old, start)
    while abs(sum(degrees) / (size * (size - 1)) - (density / 100)) > abs((sum(degrees) + 6) / (size * (size - 1)) - (density / 100)):
        check_list = [i for i in range(size)]
        first, second, third = first_second_third(data, degrees, check_list, size)
        if first is None:
            break
        join(data, degrees, first, second)
        join(data, degrees, second, third)
        join(data, degrees, third, first)
    cm.pklwrite(Pretty(data), "hamilton.pkl")
    return "Graph generated successfully."


if __name__ == "__main__":
    if not os.path.isfile("input.txt"):
        with open("input.txt", 'w') as goal:
            pass
    cm.main()