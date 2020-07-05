import command_maker as cm
import random
import os
import copy
import numpy
import timeit
import matplotlib.pyplot as plt


class Handler(cm.Controller):
    def __init__(self):
        super().__init__()


handler = Handler()
handler.commands = cm.controller.commands


@cm.add_to_switch(switch=handler.commands)
@cm.correctness
def create():
    """
    Uses options from settings: stop -> number of items, constant -> volume, to create data for further testing.
    :return:
    """
    random.seed(cm.external["seed"])
    result = [[0, 0] for _ in range(cm.external["stop"])]
    sigma = 0
    for i in range(cm.external["stop"]):
        result[i][0] = random.randint(1, cm.external["max_value"] + 1)
        result[i][1] = random.randint(1, cm.external["constant"] + 1)
        sigma += result[i][1]
    while sigma <= cm.external["constant"]:
        result[random.randint(0, cm.external["stop"])][1] += 1
        sigma += 1
    cm.jsonwrite(result, "data.json")
    cm.external.save(target="used.json")
    return "Data generated successully"


@cm.add_to_switch(switch=handler.commands, name="print")
@cm.correctness
def n_print():
    """
    Prints the data from data.json file
    :return:
    """
    internal = cm.Settings(source="used.json")
    if not internal.load():
        return "Generate the data first."
    result = ""
    data = cm.jsonread("data.json")
    result += f"Max volume = {internal['constant']}\nNumber of items = {internal['stop']}\n"
    result += "value | volume"
    for i, j in data:
        result += f"\n{i:5} | {j:6}"
    return result


def brute_force(data: list, volume: int):
    """
    Brute force implementation
    :param data:
    :param volume:
    :return:
    """
    data = sorted(data, key=lambda key: key[1])
    solution = []
    sigma = 0
    path = []
    current = 0
    i = 0
    while True:
        if i >= len(data) or data[i][1] > volume:
            if current > sigma:
                solution = list(path)
                sigma = current
            if not path:
                break
            i = path.pop() + 1
            volume += data[i - 1][1]
            current -= data[i - 1][0]
            continue
        path.append(i)
        volume -= data[i][1]
        current += data[i][0]
        i += 1
    return sigma, solution


@cm.add_to_switch(switch=handler.commands, name="brute_force")
@cm.correctness
def force():
    """
    Seeks for an optimal solution of the knapsack problem using brute force algorythm
    :return:
    """
    internal = cm.Settings(source="used.json")
    if not internal.load():
        return "Generate the data first."
    result = ""
    data = cm.jsonread("data.json")
    data = sorted(data, key=lambda key: key[1])
    sigma, solution = brute_force(data, internal["constant"])
    result += f"Max volume = {internal['constant']}\nAchieved value = {sigma}\n"
    result += "value | volume"
    for i in solution:
        result += f"\n{data[i][0]:5} | {data[i][1]:6}"
    return result


def dynamic_main(data:list, memory: dict, volume: int, node: int):
    """
    Main recursive function
    :param data:
    :param memory:
    :param volume:
    :return:
    """
    if node == -1 or volume == 0:
        return 0
    if memory.get(f"{node}|{volume}"):
        return memory[f"{node}|{volume}"]
    if data[node][1] > volume:
        memory[f"{node}|{volume}"] = dynamic_main(data, memory, volume, node - 1)
        return memory[f"{node}|{volume}"]
    memory[f"{node}|{volume}"] = max(dynamic_main(data, memory, volume, node - 1), \
                                     dynamic_main(data, memory, volume - data[node][1], node - 1) + data[node][0])
    return memory[f"{node}|{volume}"]


def path_find(data: list, memory: dict, volume: int, node: int):
    """
    Path finding
    :param data:
    :param memory:
    :param volume:
    :param node:
    :return:
    """
    path = []
    while node >= 0 and volume > 0:
        if node == 0:
            if volume > 0:
                path.append(node)
            break
        if memory[f"{node - 1}|{volume}"] == memory[f"{node}|{volume}"]:
            node -= 1
            continue
        path.append(node)
        volume -= data[node][1]
        node -= 1
    return path


def dynamic(data: list, volume: int):
    """
    Dynamic programming implementation
    :param data: 
    :param volume: 
    :return: 
    """
    memory = {}
    value = dynamic_main(data, memory, volume, len(data) - 1)
    path = path_find(data, memory, volume, len(data) - 1)
    return value, path


@cm.add_to_switch(switch=handler.commands, name="dynamic")
@cm.correctness
def dyn():
    """
    Seeks for an optimal solution of the knapsack problem using dynamic programming
    :return:
    """
    internal = cm.Settings(source="used.json")
    if not internal.load():
        return "Generate the data first."
    result = ""
    data = cm.jsonread("data.json")
    data = sorted(data, key=lambda key: key[1])
    sigma, solution = dynamic(data, internal["constant"])
    result += f"Max volume = {internal['constant']}\nAchieved value = {sigma}\n"
    result += "value | volume"
    for i in solution:
        result += f"\n{data[i][0]:5} | {data[i][1]:6}"
    return result


def check_name(name: str):
    number = 1
    while os.path.isdir(name + str(number)):
        number += 1
    return name + str(number)

@cm.add_to_switch(switch=handler.commands)
@cm.correctness
def gen_data(type: str) -> str:
    """
    Generates graphs for time measurements
    :param type: V for constant volume, N for constant number of items, all for both
    :return:
    """
    if type not in ['V', 'N', "all"]:
        return f"{type} is not an available option."
    os.mkdir((name := check_name("results/data_batch")))
    internal = cm.Settings(source=f"{name}/settings.json")
    internal.tags = copy.deepcopy(cm.external.tags)
    internal.new('V', False, "Constant Volume")
    internal.new('N', False, "Constant Number of items")
    if type == "all" or type == 'V':
        internal.change('V', True)
        bar = cm.Bar(internal["number"] * internal["different"], 0, prefix="Constant Volume")
        bar.show()
        random.seed(internal["seed"])
        for d in range(internal["different"]):
            for size in range(internal["stop"] - (internal["number"] - 1) * internal["step"], internal["stop"] + 1, \
                              internal["step"]):
                data = [[0, 0] for _ in range(size)]
                sigma = 0
                for i in range(size):
                    data[i][0] = random.randint(1, internal["max_value"] + 1)
                    data[i][1] = random.randint(1, internal["constant"] + 1)
                    sigma += data[i][1]
                while sigma <= internal["constant"]:
                    data[random.randint(0, size)][1] += 1
                    sigma += 1
                cm.pklwrite(data, f"{name}/volume-{d}_{size}.pkl")
                bar.next()
        bar.end()
        del bar
    if type == "all" or type == 'N':
        internal.change('N', True)
        bar = cm.Bar(internal["number"] * internal["different"], 0, prefix="Constant Volume")
        bar.show()
        random.seed(internal["seed"])
        for d in range(internal["different"]):
            for volume in range(internal["stop"] - (internal["number"] - 1) * internal["step"], internal["stop"] + 1, \
                                internal["step"]):
                data = [[0, 0] for _ in range(internal["constant"])]
                sigma = 0
                for i in range(internal["constant"]):
                    data[i][0] = random.randint(1, internal["max_value"] + 1)
                    data[i][1] = random.randint(1, volume + 1)
                    sigma += data[i][1]
                while sigma <= volume:
                    data[random.randint(0, internal["constant"])][1] += 1
                    sigma += 1
                cm.pklwrite(data, f"{name}/number-{d}_{volume}.pkl")
                bar.next()
        bar.end()
        del bar
    internal.save()
    return "Test data generated successfully."


def pass_data(func, data, volume):
    def pass_data_wrapper():
        func(data, volume)
    return pass_data_wrapper


def average(step: list):
    if len(step) >= 3:
        step.remove(max(step))
        step.remove(min(step))
        step.remove(max(step))
        step.remove(min(step))
    return sum(step) / len(step)


# def average(step: list):
#     average = sum(step) / len(step)
#     return min(step, key=lambda key: abs(key - average))


@cm.add_to_switch(switch=handler.commands)
@cm.correctness
def process_data(batch: int, type: str) -> str:
    """
    Processes a chosen data batch
    :param batch: A number corresponding to an existing data_batch ex. 1, 2
    :param type: V for constant volume, N for constant number of items, all for both
    :return:
    """
    if type not in ['V', 'N', "all"]:
        return f"{type} is not an available option."
    internal = cm.Settings(source=f"results/data_batch{batch}/settings.json")
    if not internal.load():
        return f"results/data_batch{batch} dir does not exist or was corrupted, generate data first."
    os.mkdir((name := check_name("results/processed_data_batch")))
    if type == "all" or type == 'V':
        if not internal['V']:
            return "test data with constant volume is not present in this data batch"
        bar = cm.Bar(internal["number"] * 2 * internal["different"], 0, prefix="Constant Volume")
        bar.show()
        step_1 = []
        step_2 = []
        force_save = []
        dynamic_save = []
        for size in range(internal["stop"] - (internal["number"] - 1) * internal["step"], internal["stop"] + 1, \
                          internal["step"]):
            for i in range(internal["different"]):
                data = cm.pklread(f"results/data_batch{batch}/volume-{i}_{size}.pkl")
                step_1.append(timeit.timeit(stmt=pass_data(dynamic, data, internal["constant"]), \
                                             number=internal["repetitions"]) / internal["repetitions"])
                bar.next()
                step_2.append(timeit.timeit(stmt=pass_data(brute_force, data, internal["constant"]), \
                                             number=internal["repetitions"]) / internal["repetitions"])
                bar.next()
            dynamic_save.append(average(step_1))
            force_save.append(average(step_2))
        bar.end()
        del bar
        numpy.savetxt(f"{name}/volume-dynamic.csv", numpy.asarray(dynamic_save))
        numpy.savetxt(f"{name}/volume-force.csv", numpy.asarray(force_save))

    if type == "all" or type == 'N':
        if not internal['N']:
            return "test data with constant number of items is not present in this data batch"
        bar = cm.Bar(internal["number"] * 2 * internal["different"], 0, prefix="Constant Number of Items")
        bar.show()
        step_1 = []
        step_2 = []
        force_save = []
        dynamic_save = []
        for volume in range(internal["stop"] - (internal["number"] - 1) * internal["step"], internal["stop"] + 1, \
                          internal["step"]):
            for i in range(internal["different"]):
                data = cm.pklread(f"results/data_batch{batch}/number-{i}_{volume}.pkl")
                step_1.append(timeit.timeit(stmt=pass_data(dynamic, data, volume), \
                                                  number=internal["repetitions"]) / internal["repetitions"])
                bar.next()
                step_2.append(timeit.timeit(stmt=pass_data(brute_force, data, volume), \
                                                number=internal["repetitions"]) / internal["repetitions"])
                bar.next()
            dynamic_save.append(average(step_1))
            force_save.append(average(step_2))
        bar.end()
        del bar
        numpy.savetxt(f"{name}/number-dynamic.csv", numpy.asarray(dynamic_save))
        numpy.savetxt(f"{name}/number-force.csv", numpy.asarray(force_save))
    internal.save(f"{name}/settings.json")
    return "Test data processed successfully."


@cm.add_to_switch(switch=handler.commands)
@cm.correctness
def plot_data(batch: int):
    """
    Plots a chosen processed data batch
    :param batch: A number corresponding to an existing processed_data_batch ex. 1, 2
    :return:
    """
    internal = cm.Settings(source=f"results/processed_data_batch{batch}/settings.json")
    if not internal.load():
        return f"results/processed_data_batch{batch} dir does not exist or was corrupted, generate data first."
    os.mkdir((name := check_name("results/figures_batch")))
    x = numpy.arange(internal["stop"] - (internal["number"] - 1) * internal["step"], internal["stop"] + 1, \
                     internal["step"])
    if internal['V']:
        y = numpy.loadtxt(f"results/processed_data_batch{batch}/volume-dynamic.csv")
        plt.plot(x, y, marker='o', label="Dynamic programming")
        y = numpy.loadtxt(f"results/processed_data_batch{batch}/volume-force.csv")
        plt.plot(x, y, marker='o', label="Brute-force")
        plt.title(f"Knapsack problem - constant capacity {internal['constant']}")
        plt.legend()
        plt.xlabel("Number of available items")
        plt.ylabel("Time [s]")
        plt.grid(True)
        for add_on in ["linear", "log"]:
            plt.yscale(add_on)
            plt.savefig(f"{name}/volume-{add_on}.png")
        plt.clf()
    if internal['N']:
        y = numpy.loadtxt(f"results/processed_data_batch{batch}/number-dynamic.csv")
        plt.plot(x, y, marker='o', label="Dynamic programming")
        y = numpy.loadtxt(f"results/processed_data_batch{batch}/number-force.csv")
        plt.plot(x, y, marker='o', label="Brute-force")
        plt.title(f"Knapsack problem - constant number of available items {internal['constant']}")
        plt.legend()
        plt.xlabel("Knapsacks capacity")
        plt.ylabel("Time [s]")
        plt.grid(True)
        for add_on in ["linear", "log"]:
            plt.yscale(add_on)
            plt.savefig(f"{name}/number-{add_on}.png")
        plt.clf()
    internal.save(f"{name}/settings.json")
    return "Figures created successfully."


if __name__ == "__main__":
    if not cm.external.load():
        cm.external.new("number", 10, "Number of tests")
        cm.external.new("stop", 15, "The largest test value.")
        cm.external.new("step", 1, "A Difference between test cases")
        cm.external.new("constant", 15, "A Value used as C or N")
        cm.external.new("max_value", 10, "The maximum possible value of one object.")
        cm.external.new("seed", 12345678, "The seed for the randomizer.")
        cm.external.new("repetitions", 10, \
                    "The Number of times one test will be redone in order to eliminate other factors")
        cm.external.new("different", 10, "The number of different test cases that will be genereated")
        cm.external.save()
    if not os.path.isdir("results"):
        os.mkdir("results")
    cm.main()
