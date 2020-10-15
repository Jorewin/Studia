import command_maker as cm
import os.path
import timeit
import types
import functools
import copy
import random
import numpy
import matplotlib.pyplot as plt


class Pretty(list):
    def __str__(self):
        result = [str(i) for i in self]
        return "\n".join(result)


class Handler(cm.Controller):
    def __init__(self):
        self.create_modes = {}
        self.traverse_modes = {}
        self.sort_modes = {}
        self.undirected = {}
        self.print_modes = {}
        self.find_modes = {}
        super().__init__()


handler = Handler()
handler.commands = cm.controller.commands


general = cm.Settings()


@cm.add_to_switch(switch=handler.commands)
def show() -> str:
    """
    Shows current settings
    :return:
    """
    result = "Current settings:\n"
    for tag in sorted(general.tags):
        result += f"{tag:20}: {general[tag]:5} -> {general.desc(tag)}\n"
    return result


@cm.add_to_switch(switch=handler.commands, name="set")
@cm.correctness
def myset(key: str, value: int) -> str:
    """
    Allows to change chosen [key] setting to [value]
    :param key:
    :param value:
    :return:
    """
    general.change(key, value)
    general.save()
    return "Setiing saved successfuly"


@cm.add_to_switch(switch=handler.print_modes)
@cm.add_to_switch(switch=handler.create_modes)
def matrix(data):
    """Adjacency matrix"""
    data = Pretty(data)
    return data


@cm.add_to_switch(switch=handler.print_modes)
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


@cm.add_to_switch(switch=handler.print_modes)
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
@cm.availability(switch=handler.print_modes, name="representation types")
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


def dfs_sort(func: types.FunctionType, data: list):
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


@cm.add_to_switch(switch=handler.sort_modes)
@cm.add_to_switch(switch=handler.traverse_modes)
def dfs_matrix(data: list, start: int = 0, check_list: list = None, path: list = None):
    """dfs - Adjacency matrix"""
    yield 0, -1, start
    if check_list is None:
        check_list = [0 for _ in data]
    if path is None:
        path = []
    path.append(start)
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
        if check_list[j] == 1 and data[path[-1]][j] == 1:
            yield 1, path[-1], j
        if check_list[j] == 0 and data[path[-1]][j] == 1:
            yield 0, path[-1], j
            path.append(j)
            check_list[j] = 1
            j = 0
        else:
            j += 1


@cm.add_to_switch(switch=handler.sort_modes)
@cm.add_to_switch(switch=handler.traverse_modes)
def dfs_table(data: list, start: int = 0, check_list: list = None):
    """dfs - Adjacency list"""
    yield 0, -1, start
    if check_list is None:
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
        if check_list[data[path[-1]][j]] == 1:
            yield 1, path[-1], data[path[-1]][j]
        if check_list[data[path[-1]][j]] == 0:
            yield 0, path[-1], data[path[-1]][j]
            check_list[data[path[-1]][j]] = 1
            path.append(data[path[-1]][j])
            j = 0
        else:
            j += 1


@cm.add_to_switch(switch=handler.sort_modes)
@cm.add_to_switch(switch=handler.traverse_modes)
def dfs_list(data: list, start: int = 0, check_list: list = None):
    """dfs - List of edges"""
    if check_list is None:
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
        if data[j][0] == path[-1] and check_list[data[j][1]] == 1:
            yield 1, path[-1], data[j][1]
        if data[j][0] == path[-1] and check_list[data[j][1]] == 0:
            yield 0, path[-1], data[j][1]
            check_list[data[j][1]] = 1
            path.append(data[j][1])
            j = 0
        else:
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


@cm.add_to_switch(switch=handler.commands, name="sort")
@cm.availability(switch=handler.sort_modes, name="sorting algorythms")
@cm.correctness
def new_sort(type: str) -> str:
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
            for i, j, k in dfs_sort(func, data):
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


@cm.add_to_switch(switch=handler.undirected)
def cycles(size: int, density: int):
    """
    Creates a directed graph with hamilton's and euler's cycle
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
    return data


@cm.add_to_switch(switch=handler.undirected)
def no_cycles(size: int, density: int):
    data = cycles(size, density)
    v = len(data) - 1
    for i in range(len(data)):
        data[i][v] = 0
        data[v][i] = 0
    return data


@cm.add_to_switch(switch=handler.commands)
@cm.availability(switch=handler.undirected, name="undirected graphs")
@cm.correctness
@cm.add_to_switch(switch=handler.print_modes, name="undirected")
def create_undirected(type: str, size: int, density: int) -> str:
    """
    Creates an undirected graph of chosen type
    :param type:
    :param size:
    :param density:
    :return:
    """
    if (func := handler.undirected.get(type)) is not None:
        cm.pklwrite(Pretty(func(size, density)), "undirected.pkl")
        return "Graph successfully created"
    else:
        return f"{type} is not an available undirected graph."


@cm.add_to_switch(switch=handler.find_modes)
def hamilton(data: list):
    check_list = [0 for _ in range(len(data))]
    path = []
    for i, j, k in dfs_matrix(data, 0, check_list=check_list, path=path):
        if len(path) == len(data) and path[0] == k:
            return path + [k]
        if i == 2:
            check_list[k] = 0
    else:
        return []


@cm.add_to_switch(switch=handler.find_modes)
def euler(data: list):
    check_list = [0 for _ in range(len(data))]
    cycle = []
    for i, j, k in dfs_matrix(data, 0, check_list=check_list):
        if i == 2:
            cycle.append(k)
        if i == 1:
            check_list[k] = 0
        if i == 0 and j != -1:
            data[j][k] = 0
            data[k][j] = 0
    else:
        cycle.append(j)
    return cycle


@cm.add_to_switch(switch=handler.commands)
@cm.availability(switch=handler.find_modes, name="find modes")
@cm.correctness
def find(type: str) -> str:
    """
    Attemps to find a chosen cycle.
    :param type:
    :return:
    """
    if (func := handler.find_modes.get(type)) is None:
        return f"{type} is not an available find mode."
    if os.path.isfile("undirected.pkl"):
        data = cm.pklread("undirected.pkl")
        if (result := func(data)):
            return str(result)
        else:
            return f"{type}'s cycle doesn't exist."
    else:
        return "Generate the data first"


def check_name(name: str):
    if not os.path.isdir(name):
        return name
    number = 1
    while os.path.isdir(name + str(number)):
        number += 1
    return name + str(number)


@cm.add_to_switch(switch=handler.commands)
@cm.correctness
def gen_data(type: str) -> str:
    """
    Generates graphs for time measurements
    :param type: directed or undirected_cycles or undirected_no_cycles or all
    :return:
    """
    if type not in ["directed", "undirected_cycles", "undirected_no_cycles", "all"]:
        return f"{type} is not an available option."
    os.mkdir((name := check_name("graphs/batch")))
    internal = cm.Settings(source=f"{name}/settings.json")
    internal.tags = copy.deepcopy(general.tags)
    internal.new("d", False, "Directed")
    internal.new("uc", False, "Undirected_cycles")
    internal.new("unc", False, "Undirected_no_cycles")
    if type == "all" or type == "directed":
        internal.change("d", True)
        bar = cm.Bar(general["number"] * 3, 0, prefix="Directed")
        bar.show()
        for size in range(general["start"], general["start"] + general["number"] * general["step"],
                          general["step"]):
            data = [[0 for _ in range(size)] for _ in range(size)]
            for i in range(size - 1):
                for j in range(i + 1, size):
                    data[i][j] = 1
            for mode in handler.create_modes:
                result = handler.create_modes[mode](data)
                cm.pklwrite(result, f"{name}/{mode}-{size}.pkl")
                bar.next()
        bar.end()
        del bar
    if type == "all" or type == "undirected_cycles":
        internal.change("uc", True)
        bar = cm.Bar(general["number"] * 2, 0, prefix="Undirected_cycles")
        bar.show()
        for size in range(general["start"], general["start"] + general["number"] * general["step"],
                          general["step"]):
            cm.pklwrite(cycles(size, 30), f"{name}/cycles(30%)-{size}.pkl")
            bar.next()
            cm.pklwrite(cycles(size, 70), f"{name}/cycles(70%)-{size}.pkl")
            bar.next()
        bar.end()
        del bar
    if type == "all" or type == "undirected_no_cycles":
        internal.change("unc", True)
        bar = cm.Bar(general["number"], 0, prefix="Undirected_no_cycles")
        bar.show()
        for size in range(general["start"], general["start"] + general["number"] * general["step"], \
                          general["step"]):
            cm.pklwrite(no_cycles(size, 50), f"{name}/no_cycles-{size}.pkl")
            bar.next()
        bar.end()
        del bar
    internal.save()
    del internal
    return "Graphs generated successfully."


def pass_data(func, data):
    def traverse_wrapper():
        for _ in func(data):
            pass
    return traverse_wrapper


def dfs_sort_decorator(func, data):
    def dfs_sort_wrapper():
        for _ in dfs_sort(func, data):
            pass
    return dfs_sort_wrapper


def pass_source(func, source):
    def pass_wrapper():
        func(source)
    return pass_wrapper


@cm.add_to_switch(switch=handler.commands)
@cm.correctness
def process_data(batch: str, type: str) -> str:
    """
    Processes a chosen data batch
    :param batch: example batch1
    :param type: directed or undirected_cycles or undirected_no_cycles or all
    :return:
    """
    if type not in ["directed", "hamilton_cycles", "euler", "hamilton_no_cycles", "all"]:
        return f"{type} is not an available option."
    internal = cm.Settings(source=f"graphs/{batch}/settings.json")
    if not internal.load():
        return f"graphs/{batch} dir does not exist or was corrupted, generate data first."
    os.mkdir((name := check_name("data/batch")))

    # Traversal and  sorting
    if type == "all" or type == "directed":
        if not internal['d']:
            return "directed graphs are not present in this data batch"
        bar = cm.Bar(internal["number"] * 12, 0, "Directed")
        bar.show()
        traversal_dfs_matrix = []
        traversal_dfs_table = []
        traversal_dfs_list = []
        traversal_bfs_matrix = []
        traversal_bfs_table = []
        traversal_bfs_list = []
        sort_dfs_matrix = []
        sort_dfs_table = []
        sort_dfs_list = []
        sort_bfs_matrix = []
        sort_bfs_table = []
        sort_bfs_list = []
        for size in range(general["start"], general["start"] + general["number"] * general["step"], \
                          general["step"]):
            # matrix
            data = cm.pklread(f"graphs/{batch}/matrix-{size}.pkl")
            traversal_dfs_matrix.append(timeit.timeit(stmt=pass_data(dfs_matrix, data), \
                                                      number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
            traversal_bfs_matrix.append(timeit.timeit(stmt=pass_data(bfs_matrix, data), \
                                                      number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
            sort_dfs_matrix.append(timeit.timeit(stmt=dfs_sort_decorator(dfs_matrix, data), \
                                                      number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
            sort_bfs_matrix.append(timeit.timeit(stmt=pass_data(bfs_matrix_sort, data), \
                                                      number=internal["repetitions"]) / internal["repetitions"])
            bar.next()

            # table
            data = cm.pklread(f"graphs/{batch}/table-{size}.pkl")
            traversal_dfs_table.append(timeit.timeit(stmt=pass_data(dfs_table, data), \
                                                      number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
            traversal_bfs_table.append(timeit.timeit(stmt=pass_data(bfs_table, data), \
                                                     number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
            sort_dfs_table.append(timeit.timeit(stmt=dfs_sort_decorator(dfs_table, data), \
                                                     number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
            sort_bfs_table.append(timeit.timeit(stmt=pass_data(bfs_table_sort, data), \
                                                     number=internal["repetitions"]) / internal["repetitions"])
            bar.next()

            # lists
            data = cm.pklread(f"graphs/{batch}/lists-{size}.pkl")
            traversal_dfs_list.append(timeit.timeit(stmt=pass_data(dfs_list, data), \
                                                      number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
            traversal_bfs_list.append(timeit.timeit(stmt=pass_data(bfs_list, data), \
                                                      number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
            sort_dfs_list.append(timeit.timeit(stmt=dfs_sort_decorator(dfs_list, data), \
                                                    number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
            sort_bfs_list.append(timeit.timeit(stmt=pass_data(bfs_list_sort, data), \
                                                    number=internal["repetitions"]) / internal["repetitions"])
            bar.next()
        bar.end()
        del bar
        numpy.savetxt(f"{name}/traversal_dfs_matrix.csv", numpy.asarray(traversal_dfs_matrix))
        numpy.savetxt(f"{name}/traversal_dfs_table.csv", numpy.asarray(traversal_dfs_table))
        numpy.savetxt(f"{name}/traversal_dfs_list.csv", numpy.asarray(traversal_dfs_list))
        numpy.savetxt(f"{name}/traversal_bfs_matrix.csv", numpy.asarray(traversal_bfs_matrix))
        numpy.savetxt(f"{name}/traversal_bfs_table.csv", numpy.asarray(traversal_bfs_table))
        numpy.savetxt(f"{name}/traversal_bfs_list.csv", numpy.asarray(traversal_bfs_list))
        numpy.savetxt(f"{name}/sort_dfs_matrix.csv", numpy.asarray(sort_dfs_matrix))
        numpy.savetxt(f"{name}/sort_dfs_table.csv", numpy.asarray(sort_dfs_table))
        numpy.savetxt(f"{name}/sort_dfs_list.csv", numpy.asarray(sort_dfs_list))
        numpy.savetxt(f"{name}/sort_bfs_matrix.csv", numpy.asarray(sort_bfs_matrix))
        numpy.savetxt(f"{name}/sort_bfs_table.csv", numpy.asarray(sort_bfs_table))
        numpy.savetxt(f"{name}/sort_bfs_list.csv", numpy.asarray(sort_bfs_list))
    else:
        internal.change('d', False)

    # Hamilton with cycles
    if type == "all" or type == "hamilton_cycles":
        if not internal["uc"]:
            return "undirected graphs with cycles are not present in this data batch"
        bar = cm.Bar(internal["number"] * 2, 0, "Hamilton_cycles")
        hamilton30_cycles = []
        hamilton70_cycles = []
        bar.show()
        for size in range(general["start"], general["start"] + general["number"] * general["step"], \
                          general["step"]):
            data = cm.pklread(f"graphs/{batch}/cycles(30%)-{size}.pkl")
            hamilton30_cycles.append(timeit.timeit(stmt=pass_source(hamilton, data), \
                                                 number=general["repetitions"]) / general["repetitions"])
            bar.next()
            data = cm.pklread(f"graphs/{batch}/cycles(70%)-{size}.pkl")
            hamilton70_cycles.append(timeit.timeit(stmt=pass_source(hamilton, data), \
                                                   number=general["repetitions"]) / general["repetitions"])
            bar.next()
        bar.end()
        del bar
        numpy.savetxt(f"{name}/hamilton(30%).csv", numpy.asarray(hamilton30_cycles))
        numpy.savetxt(f"{name}/hamilton(70%).csv", numpy.asarray(hamilton70_cycles))
        internal.new("hc", True, "Hamilton_cycles")
    else:
        internal.new("hc", False, "Hamilton_cycles")

    # Euler
    if type == "all" or type == "euler":
        if not internal["uc"]:
            return "undirected graphs with cycles are not present in this data batch"
        bar = cm.Bar(internal["number"] * 2, 0, "Euler")
        euler30_cycles = []
        euler70_cycles = []
        bar.show()
        for size in range(general["start"], general["start"] + general["number"] * general["step"], \
                          general["step"]):
            data = cm.pklread(f"graphs/{batch}/cycles(30%)-{size}.pkl")
            euler30_cycles.append(timeit.timeit(stmt=pass_source(euler, data), \
                                                number=general["repetitions"]) / general["repetitions"])
            bar.next()
            data = cm.pklread(f"graphs/{batch}/cycles(70%)-{size}.pkl")
            euler70_cycles.append(timeit.timeit(stmt=pass_source(euler, data), \
                                                number=general["repetitions"]) / general["repetitions"])
            bar.next()
        bar.end()
        del bar
        numpy.savetxt(f"{name}/euler(30%).csv", numpy.asarray(euler30_cycles))
        numpy.savetxt(f"{name}/euler(70%).csv", numpy.asarray(euler70_cycles))
        internal.new("e", True, "Euler")
    else:
        internal.new("e", False, "Euler")

    # Hamilton without cycles
    if type == "all" or type == "hamilton_no_cycles":
        if not internal["unc"]:
            return "undirected graphs without cycles are not present in this data batch"
        bar = cm.Bar(internal["number"], 0, "Undirected_no_cycles")
        hamilton50_no_cycles = []
        bar.show()
        for size in range(general["start"], general["start"] + general["number"] * general["step"], \
                          general["step"]):
            data = cm.pklread(f"graphs/{batch}/no_cycles-{size}.pkl")
            hamilton50_no_cycles.append(timeit.timeit(stmt=pass_source(hamilton, data), \
                                                 number=general["repetitions"]) / general["repetitions"])
            bar.next()
        bar.end()
        del bar
        numpy.savetxt(f"{name}/hamilton(50%).csv", numpy.asarray(hamilton50_no_cycles))
        internal.new("hnc", True, "Hamilton_no_cycles")
    else:
        internal.new("hnc", False, "Hamilton_no_cycles")
    internal.save(target=f"{name}/settings.json")
    return "Data processed successfully"


@cm.add_to_switch(switch=handler.commands)
@cm.correctness
def plot_data(batch: str) -> str:
    """
    Plots a chosen data batch
    :param batch: example batch1
    :return:
    """
    internal = cm.Settings(source=f"data/{batch}/settings.json")
    if not internal.load():
        return f"data/{batch} dir does not exist or was corrupted, generate data first."
    os.mkdir((name := check_name("figures/batch")))

    # Traversal and sorting
    if internal['d']:
        x = numpy.arange(internal["start"], internal["start"] + internal["number"] * internal["step"], \
                          internal["step"])
        plt.plot([0], marker='None', linestyle='None', label='DFS')
        y = numpy.loadtxt(f"data/{batch}/traversal_dfs_matrix.csv")
        plt.plot(x, y, marker='o', label="adjacency matrix")
        y = numpy.loadtxt(f"data/{batch}/traversal_dfs_table.csv")
        plt.plot(x, y, marker='o', label="adjacency list")
        y = numpy.loadtxt(f"data/{batch}/traversal_dfs_list.csv")
        plt.plot(x, y, marker='o', label="list of edges")
        plt.plot([0], marker='None', linestyle='None', label='BFS')
        y = numpy.loadtxt(f"data/{batch}/traversal_bfs_matrix.csv")
        plt.plot(x, y, marker='o', label="adjacency matrix")
        y = numpy.loadtxt(f"data/{batch}/traversal_bfs_table.csv")
        plt.plot(x, y, marker='o', label="adjacency list")
        y = numpy.loadtxt(f"data/{batch}/traversal_dfs_list.csv")
        plt.plot(x, y, marker='o', label="list of edges")
        plt.title("Graph traversal")
        plt.legend()
        plt.xlabel("Number of vertices in the graph")
        plt.ylabel("Time [s]")
        plt.grid(True)
        for add_on in ["linear", "log"]:
            plt.yscale(add_on)
            plt.savefig(f"{name}/traversal-{add_on}.png")
        plt.clf()
        plt.plot([0], marker='None', linestyle='None', label='DFS')
        y = numpy.loadtxt(f"data/{batch}/sort_dfs_matrix.csv")
        plt.plot(x, y, marker='o', label="adjacency matrix")
        y = numpy.loadtxt(f"data/{batch}/sort_dfs_table.csv")
        plt.plot(x, y, marker='o', label="adjacency list")
        y = numpy.loadtxt(f"data/{batch}/sort_dfs_list.csv")
        plt.plot(x, y, marker='o', label="list of edges")
        plt.plot([0], marker='None', linestyle='None', label='BFS')
        y = numpy.loadtxt(f"data/{batch}/sort_bfs_matrix.csv")
        plt.plot(x, y, marker='o', label="adjacency matrix")
        y = numpy.loadtxt(f"data/{batch}/sort_bfs_table.csv")
        plt.plot(x, y, marker='o', label="adjacency list")
        y = numpy.loadtxt(f"data/{batch}/sort_dfs_list.csv")
        plt.plot(x, y, marker='o', label="list of edges")
        plt.title("Topological sort")
        plt.legend()
        plt.xlabel("Number of vertices in the graph")
        plt.ylabel("Time [s]")
        plt.grid(True)
        for add_on in ["linear", "log"]:
            plt.yscale(add_on)
            plt.savefig(f"{name}/sort-{add_on}.png")
        plt.clf()

    # Hamilton with cycles
    if internal["hc"]:
        x = numpy.arange(internal["start"], internal["start"] + internal["number"] * internal["step"], \
                         internal["step"])
        y = numpy.loadtxt(f"data/{batch}/hamilton(30%).csv")
        plt.plot(x, y, marker='o', label="30% graph density")
        y = numpy.loadtxt(f"data/{batch}/hamilton(70%).csv")
        plt.plot(x, y, marker='o', label="70% graph density")
        plt.title("Finding Hamilton's cycle")
        plt.legend()
        plt.xlabel("Number of vertices in the graph")
        plt.ylabel("Time [s]")
        plt.grid(True)
        for add_on in ["linear", "log"]:
            plt.yscale(add_on)
            plt.savefig(f"{name}/true-hamilton-{add_on}.png")

    # Euler
    if internal["e"]:
        x = numpy.arange(internal["start"], internal["start"] + internal["number"] * internal["step"], \
                         internal["step"])
        y = numpy.loadtxt(f"data/{batch}/euler(30%).csv")
        plt.plot(x, y, marker='o', label="30% graph density")
        y = numpy.loadtxt(f"data/{batch}/euler(70%).csv")
        plt.plot(x, y, marker='o', label="70% graph density")
        plt.title("Finding Euler's cycle")
        plt.legend()
        plt.xlabel("Number of vertices in the graph")
        plt.ylabel("Time [s]")
        plt.grid(True)
        for add_on in ["linear", "log"]:
            plt.yscale(add_on)
            plt.savefig(f"{name}/euler-{add_on}.png")
        plt.clf()

    # Hamilton without cycles
    if internal["hnc"]:
        x = numpy.arange(internal["start"], internal["start"] + internal["number"] * internal["step"], \
                         internal["step"])
        y = numpy.loadtxt(f"data/{batch}/hamilton(50%).csv")
        plt.plot(x, y, marker='o')
        plt.title("Finding Hamilton's cycle, graph density - 50%")
        plt.xlabel("Number of vertices in the graph")
        plt.ylabel("Time [s]")
        plt.grid(True)
        for add_on in ["linear", "log"]:
            plt.yscale(add_on)
            plt.savefig(f"{name}/false-hamilton-{add_on}.png")
        plt.clf()
    return "Data plotted successfully"


if __name__ == "__main__":
    if not general.load():
        general.new("number", 10, "Number of tests")
        general.new("start", 20, "Lenght of the shortest test case")
        general.new("step", 1, "Difference between test cases")
        general.new("repetitions", 10, \
                    "Number of times one test will be redone in order to eliminate other factors")
        general.save()
    if not os.path.isdir("graphs"):
        os.mkdir("graphs")
    if not os.path.isdir("data"):
        os.mkdir("data")
    if not os.path.isdir("figures"):
        os.mkdir("figures")
    if not os.path.isfile("input.txt"):
        with open("input.txt", 'w') as goal:
            pass
    cm.main()