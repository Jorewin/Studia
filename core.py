import command_maker as cm
import os.path
import timeit


class Pretty(list):
    def __str__(self):
        result = [str(i) for i in self]
        return "\n".join(result)


class Handler(cm.Controller):
    def __init__(self):
        self.create_modes = {}
        self.traverse_modes = {}
        super().__init__()


handler = Handler()
handler.commands = cm.controller.commands


# Create modes
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
def list(data):
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


@cm.add_to_switch(switch=handler.traverse_modes)
def dfs_matrix(data: list):
    """dfs - Adjacency matrix"""
    yield 0
    check_list = [0 for _ in data]
    path = [0]
    check_list[0] = 1
    j = 0
    while True:
        if j >= len(data):
            if len(path) == 1:
                break
            else:
                j = path.pop() + 1
                continue
        if check_list[j] != 1 and data[path[-1]][j] == 1:
            path.append(j)
            check_list[j] = 1
            yield j
            j = 0
        else:
            j += 1


@cm.add_to_switch(switch=handler.traverse_modes)
def dfs_table(data: list):
    """dfs - Adjacency list"""
    yield 0
    check_list = [0 for _ in data]
    check_list[0] = 1
    path = [0]
    j = 0
    while True:
        if j >= len(data[path[-1]]):
            if len(path) == 1:
                break
            else:
                path.pop()
                j = 0
                continue
        if check_list[data[path[-1]][j]] != 1:
            check_list[data[path[-1]][j]] = 1
            yield data[path[-1]][j]
            path.append(data[path[-1]][j])
            j = 0
        else:
            j += 1


@cm.add_to_switch(switch=handler.traverse_modes)
def dfs_list(data: list):
    """dfs - List of edges"""
    check_list = {'0': 1}
    yield 0
    path = [0]
    j = 0
    while True:
        if j >= len(data):
            if len(path) == 1:
                break
            else:
                path.pop()
                j = 0
                continue
        if data[j][0] == path[-1]:
            if check_list.get(f"{data[j][1]}") != 1:
                check_list[f"{data[j][1]}"] = 1
                yield data[j][1]
                path.append(data[j][1])
                j = 0
                continue
        j += 1


@cm.add_to_switch(switch=handler.traverse_modes)
def bfs_matrix(data: list):
    """bfs - Adjacency matrix"""
    yield 0
    check_list = [0 for _ in data]
    queue = [0]
    check_list[0] = 1
    while queue:
        for i in range(len(data)):
            if check_list[i] != 1 and data[queue[0]][i] == 1:
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
            if check_list[data[queue[0]][i]] != 1:
                yield data[queue[0]][i]
                check_list[data[queue[0]][i]] = 1
                queue.append(data[queue[0]][i])
        del queue[0]


@cm.add_to_switch(switch=handler.traverse_modes)
def bfs_list(data: list):
    """bfs - List of edges"""
    yield 0
    check_list = {'0': 1}
    queue = [0]
    check_list[0] = 1
    while queue:
        for pair in data:
            if pair[0] == queue[0] and check_list.get(f"{pair[1]}") != 1:
                yield pair[1]
                check_list[f"{pair[1]}"] = 1
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
        result = [i for i in func(data)]
        return str(result)
    else:
        return f"File {type[4::]}.pkl doesn't exist, generate data first."


@cm.add_to_switch(switch=handler.commands)
@cm.availability(switch=handler.traverse_modes, name="traversal algorythms")
@cm.correctness
def dev_traverse(type: str) -> str:
    """
    Prints the traversal road based on the chosen [type] algorythm
    :param type:
    :return:
    """
    if (func := handler.traverse_modes.get(type)) is None:
        return f"{type} is not an available traversal algorythm."
    if os.path.isfile(f"{type[4::]}.pkl"):
        data = cm.pklread(f"{type[4::]}.pkl")
        def test(func = func, data = data):
            result = [i for i in func(data)]
        time = timeit.timeit(stmt=test,number=100)
        time /= 100
        return str(time)
    else:
        return f"File {type[4::]}.pkl doesn't exist, generate data first."

if __name__ == "__main__":
    if not os.path.isfile("input.txt"):
        with open("input.txt", 'w') as goal:
            pass
    cm.main()