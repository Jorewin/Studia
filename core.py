import cmd
import copy
import random
import os.path
import json
import functools
import types
import pickle
import re
import math
import timeit
import numpy
import shutil
import datetime
import matplotlib.pyplot as plt
import sys


class Handler(cmd.Controller):
    def __init__(self):
        self.algorythms = {}
        self.readmodes = {}
        self.writemodes = {}
        self.orders = {}
        self.kinds = {}
        super().__init__()


class BSTnode():
    def __init__(self, value: int, son: int = None, daughter: int = None):
        self.value = value
        self.son = son
        self.daughter = daughter


    def __repr__(self):
        return f'BSTnode value: {self.value}, son: {self.son}, daughter: {self.daughter}'


class AVLnode(BSTnode):
    def __init__(self, value: int, son: int = None, daughter: int = None, balance: int = 0):
        super().__init__(value, son, daughter)
        self.balance = balance


    def __repr__(self):
        return f'AVLnode value: {self.value}, son: {self.son}, daughter: {self.daughter}, bf: {self.balance}'


handler = Handler()
handler.commands = cmd.controller.commands


#External function, prints progress bar
def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def iofiles(_func: types.FunctionType = None, *, source: str = None, target: str = None):
    """
    Makes algorythm use data from source and save it to target.
    :param types.FunctionType func:
    :param str source: source file
    :param str target: target file
    :return: decorated function
    :rtype: types.FunctionType
    """
    def decorator_iofiles(func):
        @functools.wraps(func)
        def wrapper_iofiles(handler: Handler, *args, **kwargs):
            if not os.path.isfile(source):
                print('Generate or enter the data first.')
                return
            if (_type := re.search('\.[A-z]+', source)) is None:
                raise ValueError('File without extension')
            if handler.readmodes.get(_type.group()) is None:
                raise ValueError(f'{_type.group()} extension is not available')
            data = handler.readmodes[_type.group()](source)
            func(handler, data, *args, **kwargs)
            if target is not None:
                if (_type := re.search('\.[A-z]+', target)) is None:
                    raise ValueError('File without extension')
                if handler.writemodes.get(_type.group()) is None:
                    raise ValueError(f'{_type.group()} extension is not available')
                handler.writemodes[_type.group()](data, target)
        return wrapper_iofiles
    if _func is None:
        return decorator_iofiles
    else:
        return decorator_iofiles(_func)


def availability(_func: types.FunctionType = None, *, toggle: dict, name: str):
    """
    Adds list to func.doc
    :param types.FunctionType _func:
    :param dict toggle:
    :param str name:
    :return:
    """
    def decorator_availability(func):
        func.__doc__ += f'Available {name}:'
        for thing in toggle:
            func.__doc__ += f'\n\t+ {thing}'
        return func
    if _func is None:
        return decorator_availability
    else:
        return decorator_availability(_func)


@cmd.addtoswitch(switch=handler.readmodes, name='.pkl')
def pklread(source: str):
    """
    Reads from pkl file
    :param str source:
    :return:
    """
    with open(source, 'rb') as origin:
        result = pickle.load(origin)
    return result


@cmd.addtoswitch(switch=handler.readmodes, name='.json')
def jsonread(source: str):
    """
    Reads from json file
    :param str source:
    :return:
    """
    with open(source, 'r') as origin:
        result = json.load(origin)
    return result


@cmd.addtoswitch(switch=handler.writemodes, name='.pkl')
def pklwrite(object, target: str):
    """
    Writes to pkl file
    :param object:
    :param str target:
    :return:
    """
    with open(target, 'wb') as goal:
        pickle.dump(object, goal)


@cmd.addtoswitch(switch=handler.writemodes, name='.json')
def jsonwrite(object, target: str):
    """
    Writes to json file
    :param object:
    :param str target:
    :return:
    """
    with open(target, 'w') as goal:
        json.dump(object, goal)


@cmd.addtoswitch(switch=handler.commands, name='settings')
@iofiles(source='settings.json', target='settings.json')
@cmd.correctness
def mysettings(handler: Handler, settings: dict, *, _e: bool = False) -> str:
    """
    Shows current settings
    :param Handler handler:
    :param dict settings:
    :param bool _e: User specified, optional, shows descriptions of settings
    :return: settings
    :rtype: str
    """
    result = ['Current settings:']
    for i, key in enumerate(sorted((settings))):
        if i%2 == 0:
            result.append(f'{key:10} -> {settings[key]}')
        elif _e:
            result.append(settings[key])
    return '\n'.join(result)


@cmd.addtoswitch(switch=handler.commands, name='set')
@iofiles(source='settings.json', target='settings.json')
@cmd.correctness
def myset(handler: Handler, settings: dict, key: str, value: int) -> str:
    """
    Allows to change setting value
    :param Handler handler:
    :param dict settings:
    :param str key: User specified
    :param int value: User specified
    :return:
    :rtype: str
    """
    result = ''
    if settings.get(key) is None or key[-1] == '!':
        return f'{key} setting not found'
    if key == 'upperlimit' and (value < 20 or value % 10 != 0):
        return 'Upperlimit must be a multiple of 10 and must be higher than 10.'
    settings[key] = value
    return 'setting saved succesfully'


@cmd.addtoswitch(switch=handler.commands)
@iofiles(source='settings.json')
@cmd.correctness
def gendata(handler: Handler, settings: dict) -> str:
    """
    Generates data for long tests
    :param Handler handler:
    :param dict settings:
    :return:
    :rtype: str
    """
    shutil.rmtree('data')
    os.mkdir('data')
    total = 10
    iteration = 0
    printProgressBar(iteration, total)
    for i in range(10, settings['upperlimit'] + 1, settings['upperlimit'] // 10):
        iteration += 1
        arr = [random.randint(0, i + 1) for _ in range(i)]
        arr = sorted(arr)[::-1]
        jsonwrite(arr, f'data/{i}.json')
        printProgressBar(iteration, total)
    jsonwrite(settings, 'data/settings.json')
    return 'Data generated successfully'


@cmd.addtoswitch(switch=handler.commands)
@iofiles(source='data/settings.json')
@cmd.correctness
def processdata(handler: Handler, settings: dict, *, _t: str = None) -> str:
    """
    Testing mechanism
    :param Handler handler:
    :param dict settings:
    :param str _t: User specified, optional, BST or AVL
    :return:
    :rtype: str
    """
    shutil.rmtree('processeddata')
    os.mkdir('processeddata')
    settings['BST'] = False
    settings['AVL'] = False
    if _t is None or _t == 'BST':
        total = 40
        iteration = 0
        printProgressBar(iteration, total)
        creating, finding, printing, DSW = [], [], [], []
        for i in range(10, settings['upperlimit'] + 1, settings['upperlimit'] // 10):
            iteration += 1

            def create():
                tree = jsonread(f'data/{i}.json')
                handler.algorythms['genbst'](handler, tree)

            tree = jsonread(f'data/{i}.json')
            handler.algorythms['genbst'](handler, tree)
            time = timeit.timeit(stmt=create, number=10)
            time /= 10
            creating.append(time)
            printProgressBar(iteration, total)
            iteration += 1

            def finder():
                handler.algorythms['find'](handler, tree, 'lowest')

            time = timeit.timeit(stmt=finder, number=10)
            time /= 10
            finding.append(time)
            printProgressBar(iteration, total)
            iteration += 1

            def printer():
                handler.algorythms['in_order2'](tree, 0)

            time = timeit.timeit(stmt=printer, number=10)
            time /= 10
            printing.append(time)
            printProgressBar(iteration, total)
            iteration += 1

            def fixer():
                handler.algorythms['dsw'](handler, tree)

            time = timeit.timeit(stmt=fixer, number=10)
            time /= 10
            DSW.append(time)
            printProgressBar(iteration, total)
        creating = numpy.asarray(creating)
        numpy.savetxt('processeddata/bst_creating.csv', creating, delimiter=',')
        finding = numpy.asarray(finding)
        numpy.savetxt('processeddata/bst_finding.csv', finding, delimiter=',')
        printing = numpy.asarray(printing)
        numpy.savetxt('processeddata/bst_printing.csv', printing, delimiter=',')
        DSW = numpy.asarray(DSW)
        numpy.savetxt(f'processeddata/bst_DSW.csv', DSW, delimiter=',')
        settings['BST'] = True
    if _t is None or _t == 'AVL':
        total = 30
        iteration = 0
        printProgressBar(iteration, total)
        creating, finding, printing = [], [], []
        for i in range(10, settings['upperlimit'] + 1, settings['upperlimit'] // 10):
            iteration += 1

            def create():
                tree = jsonread(f'data/{i}.json')
                handler.algorythms['genavl'](handler, tree)

            tree = jsonread(f'data/{i}.json')
            handler.algorythms['genavl'](handler, tree)
            time = timeit.timeit(stmt=create, number=10)
            time /= 10
            creating.append(time)
            printProgressBar(iteration, total)
            iteration += 1

            def finder():
                handler.algorythms['find'](handler, tree, 'lowest')

            time = timeit.timeit(stmt=finder, number=10)
            time /= 10
            finding.append(time)
            printProgressBar(iteration, total)
            iteration += 1

            def printer():
                handler.algorythms['in_order2'](tree, 0)

            time = timeit.timeit(stmt=printer, number=10)
            time /= 10
            printing.append(time)
            printProgressBar(iteration, total)
        creating = numpy.asarray(creating)
        numpy.savetxt('processeddata/avl_creating.csv', creating, delimiter=',')
        finding = numpy.asarray(finding)
        numpy.savetxt('processeddata/avl_finding.csv', finding, delimiter=',')
        printing = numpy.asarray(printing)
        numpy.savetxt('processeddata/avl_printing.csv', printing, delimiter=',')
        settings['AVL'] = True
    else:
        return f'{_t} is not an available tree type'
    jsonwrite(settings, 'processeddata/settings.json')
    return f'data processed successfully'


@cmd.addtoswitch(switch=handler.commands)
@iofiles(source='processeddata/settings.json')
@cmd.correctness
def plotdata(handler: Handler, settings: dict, *, _l: bool = False) -> str:
    """
    Plots data
    :param handler:
    :param settings:
    :param _l: User specified, optional, sets scale of the x axis to log
    :return:
    """
    time = datetime.datetime.now().strftime("%H_%M_%S")
    os.mkdir(f'figures/{time}')
    x = numpy.arange(10, settings['upperlimit'], settings['upperlimit'] // 10)
    if not settings['BST']:
        return 'BST data not generated'
    if not settings['BST']:
        return 'AVL data not generated'

    #Constructing
    y = numpy.loadtxt('processeddata/bst_creating.csv')
    plt.plot(x, y, marker='o', label='BST')
    y = numpy.loadtxt('processeddata/avl_creating.csv')
    plt.plot(x, y, marker='o', label='AVL')
    plt.title('Tree construction')
    plt.legend()
    plt.xlabel('Lenght of the test case')
    plt.ylabel('Time [s]')
    plt.grid(True)
    plt.savefig(f'figures/{time}/Constructing.png')
    plt.clf()

    #Finding
    y = numpy.loadtxt('processeddata/bst_finding.csv')
    plt.plot(x, y, marker='o', label='BST')
    y = numpy.loadtxt('processeddata/avl_finding.csv')
    plt.plot(x, y, marker='o', label='AVL')
    plt.title('Finding the lowest element')
    plt.legend()
    plt.xlabel('Lenght of the test case')
    plt.ylabel('Time [s]')
    plt.grid(True)
    plt.savefig(f'figures/{time}/Finding.png')
    plt.clf()

    #Printing
    y = numpy.loadtxt('processeddata/bst_printing.csv')
    plt.plot(x, y, marker='o', label='BST')
    y = numpy.loadtxt('processeddata/avl_printing.csv')
    plt.plot(x, y, marker='o', label='AVL')
    plt.title('Printing elements in order')
    plt.legend()
    plt.xlabel('Lenght of the test case')
    plt.ylabel('Time [s]')
    plt.grid(True)
    plt.savefig(f'figures/{time}/Printing')
    plt.clf()

    #DSW
    y = numpy.loadtxt('processeddata/bst_DSW.csv')
    plt.plot(x, y, marker='o')
    plt.title('DSW algorythm')
    plt.xlabel('Lenght of the test case')
    plt.ylabel('Time [s]')
    plt.grid(True)
    plt.savefig(f'figures/{time}/DSW')
    plt.clf()


@cmd.addtoswitch(switch=handler.commands)
@cmd.correctness
def enterdata(handler: Handler, arr: list) -> str:
    """
    Lets user input list into the system
    :param Handler handler:
    :param list arr: User specified, example [1,2,3,4,5]
    :return:
    :rtype: str
    """
    with open('userdata.json', 'w') as target:
        json.dump(arr, target)
    return 'Data saved successfully'


@cmd.addtoswitch(switch=handler.commands)
@cmd.correctness
def genarr(handler: Handler, lenght: int) -> str:
    """
    Generates test arr
    :param Toggle toggle:
    :param int lenght: User specified
    :return:
    :rtype: str
    """
    if lenght < 0:
        return 'Lenght must be a nonnegative integer'
    arr = [random.randint(0, lenght+1) for _ in range(lenght)]
    with open('userdata.json', 'w') as target:
        json.dump(arr, target)
    return 'Data saved successfully'


@cmd.addtoswitch(switch=handler.commands)
@cmd.correctness
def printdata(handler: Handler) -> str:
    """
    Prints data from userdata.json if the file exists
    :param Handler handler:
    :return:
    :rtype: str
    """
    if not os.path.isfile('userdata.json'):
        return 'Generate or enter the data first.'
    with open('userdata.json', 'r') as source:
        return str(json.load(source))


@cmd.addtoswitch(switch=handler.orders)
def pre_order(tree: list, p: int):
    """
    Returns keys of the tree
    :param list tree:
    :param int p:
    :return:
    """
    left, right = [], []
    if tree[p].son is not None:
        left = pre_order(tree, tree[p].son)
    if tree[p].daughter is not None:
        right = pre_order(tree, tree[p].daughter)
    return [p] + left + right


@cmd.addtoswitch(switch=handler.orders)
def pre_order2(tree: list, p: int):
    """
    Returns keys of the tree
    :param list tree:
    :param int p:
    :return:
    """
    arr = [0]
    i = 0
    while i < len(arr):
        if tree[arr[i]].daughter is not None:
            arr.insert(i+1, tree[arr[i]].daughter)
        if tree[arr[i]].son is not None:
            arr.insert(i+1, tree[arr[i]].son)
        i += 1
    return arr


@cmd.addtoswitch(switch=handler.orders)
@cmd.addtoswitch(switch=handler.algorythms)
def in_order(tree: list, p: int):
    """
    Returns keys of the tree
    :param list tree:
    :param int p:
    :return:
    """
    left, right = [], []
    if tree[p].son is not None:
        left = in_order(tree, tree[p].son)
    if tree[p].daughter is not None:
        right = in_order(tree, tree[p].daughter)
    return left + [p] + right


@cmd.addtoswitch(switch=handler.orders)
@cmd.addtoswitch(switch=handler.algorythms)
def in_order2(tree: list, p: int):
    """
    Returns keys of the tree
    :param list tree:
    :param int p:
    :return:
    """
    arr = [0]
    checklist = [0 for _ in range(len(tree))]
    i = 0
    while i < len(arr):
        if checklist[arr[i]] == 1:
            i += 1
            continue
        checklist[arr[i]] = 1
        if tree[arr[i]].daughter is not None:
            arr.insert(i + 1, tree[arr[i]].daughter)
        if tree[arr[i]].son is not None:
            arr.insert(i, tree[arr[i]].son)
    return arr


@cmd.addtoswitch(switch=handler.orders)
def post_order(tree: list, p: int):
    """
    Yields keys of the tree
    :param list tree:
    :param int p:
    :return:
    """
    left, right = [], []
    if tree[p].son is not None:
        left = post_order(tree, tree[p].son)
    if tree[p].daughter is not None:
        right = post_order(tree, tree[p].daughter)
    return left + right + [p]


@cmd.addtoswitch(switch=handler.commands)
@iofiles(source='userdata.json', target='usertree.pkl')
@cmd.correctness
@cmd.addtoswitch(switch=handler.algorythms)
def genbst(handler: Handler, arr: list) -> str:
    """
    Converts list to BST tree
    :param Toggle toggle:
    :param list arr:
    :return:
    :rtype: str
    """
    for key in range(len(arr)):
        node = BSTnode(arr[key])
        arr[key] = node
        if key == 0:
            continue
        p = 0
        while True:
            if arr[key].value < arr[p].value:
                if arr[p].son is None:
                    arr[p].son = key
                    break
                else:
                    p = arr[p].son
            else:
                if arr[p].daughter is None:
                    arr[p].daughter = key
                    break
                else:
                    p = arr[p].daughter
    return 'BST tree generated successfully'


def RR(tree: list, p: int):
    """
    RR
    :param list tree:
    :param int p:
    :return:
    """
    node = AVLnode(tree[p].value, tree[p].son, tree[p].daughter, tree[p].balance)
    pointer = tree[p].daughter
    tree[p].value = tree[pointer].value
    tree[p].daughter = tree[pointer].daughter
    tree[p].balance = tree[pointer].balance + 1
    tree[pointer].daughter = tree[pointer].son
    tree[pointer].son = node.son
    tree[pointer].value = node.value
    tree[pointer].balance = node.balance - tree[pointer].balance + 1
    tree[p].son = pointer


def RL(tree: list, p: int):
    """
    RL
    :param list tree:
    :param int p:
    :return:
    """
    node = AVLnode(tree[p].value, tree[p].son, tree[p].daughter, tree[p].balance)
    pointer = tree[tree[p].daughter].son
    tree[p].value = tree[pointer].value
    tree[p].balance = 0
    tree[tree[p].daughter].son = tree[pointer].daughter
    if tree[pointer].balance == 1:
        tree[tree[p].daughter].balance = -1
    else:
        tree[tree[p].daughter].balance = 0
    tree[pointer].daughter = tree[pointer].son
    tree[pointer].son = node.son
    tree[pointer].value = node.value
    if tree[pointer].balance == -1:
        tree[pointer].balance = 1
    else:
        tree[pointer].balance = 0
    tree[p].son = pointer


def LL(tree: list, p: int):
    """
    LL
    :param list tree:
    :param int p:
    :return:
    """
    node = AVLnode(tree[p].value, tree[p].son, tree[p].daughter, tree[p].balance)
    pointer = tree[p].son
    tree[p].value = tree[pointer].value
    tree[p].son = tree[pointer].son
    tree[p].balance = tree[pointer].balance - 1
    tree[pointer].son = tree[pointer].daughter
    tree[pointer].daughter = node.daughter
    tree[pointer].value = node.value
    tree[pointer].balance = node.balance - tree[pointer].balance - 1
    tree[p].daughter = pointer


def LR(tree: list, p: int):
    """
    LR
    :param list tree:
    :param int p:
    :return:
    """
    node = AVLnode(tree[p].value, tree[p].son, tree[p].daughter, tree[p].balance)
    pointer = tree[tree[p].son].daughter
    tree[p].value = tree[pointer].value
    tree[p].balance = 0
    tree[tree[p].son].daughter = tree[pointer].son
    if tree[pointer].balance == -1:
        tree[tree[p].son].balance = 1
    else:
        tree[tree[p].son].balance = 0
    tree[pointer].son = tree[pointer].daughter
    tree[pointer].daughter = node.daughter
    tree[pointer].value = node.value
    if tree[pointer].balance == 1:
        tree[pointer].balance = -1
    else:
        tree[pointer].balance = 0
    tree[p].daughter = pointer


def balancer(tree: list):
    """
    Balances the AVL tree
    :param list tree:
    :return:
    """
    for p in post_order(tree, 0):
        while abs(tree[p].balance) > 1:
            if tree[p].balance < -1:
                if tree[tree[p].daughter].balance <= 0:
                    RR(tree, p)
                else:
                    LL(tree, tree[p].daughter)
                    RR(tree, p)
            elif tree[p].balance > 1:
                if tree[tree[p].son].balance >= 0:
                    LL(tree, p)
                else:
                    RR(tree, tree[p].son)
                    LL(tree, p)


def balancer2(tree: list, p: int):
    """
    Balances the AVL tree
    :param list tree:
    :param int p:
    :return:
    """
    while abs(tree[p].balance) > 1:
        if tree[p].balance < -1:
            if tree[tree[p].daughter].balance <= 0:
                RR(tree, p)
            else:
                RL(tree, p)
        elif tree[p].balance > 1:
            if tree[tree[p].son].balance >= 0:
                LL(tree, p)
            else:
                LR(tree, p)


def inner(tree: list, path: list, p: int):
    if tree[path[0]].balance != 0:
        tree[path[0]].balance = 0
        return
    if tree[path[0]].son == p:
        tree[path[0]].balance = 1
    else:
        tree[path[0]].balance = -1
    p = path[0]
    r = 0
    for i in path[1::]:
        if tree[i].balance != 0:
            r = i
            break
        if tree[i].son == p:
            tree[i].balance += 1
        else:
            tree[i].balance -= 1
        p = i
    else:
        return
    if tree[r].balance == -1:
        if tree[r].son == p:
            tree[r].balance = 0
        elif tree[p].balance == 1:
            RL(tree, r)
        else:
            RR(tree, r)
    else:
        if tree[r].daughter == p:
            tree[r].balance = 0
        elif tree[p].balance == -1:
            LR(tree, r)
        else:
            LL(tree, r)


def createavl(tree: list, start: int, stop: int):
    """
    Recursive function
    :param list tree:
    :param int start:
    :param int stop:
    :return:
    """
    if stop < start:
        return
    key = (start + stop) // 2
    node = AVLnode(tree[key])
    tree[key] = node
    path = []
    p = 0
    while True:
        path.insert(0, p)
        if tree[key].value < tree[p].value:
            if tree[p].son is None:
                tree[p].son = key
                break
            else:
                p = tree[p].son
        else:
            if tree[p].daughter is None:
                tree[p].daughter = key
                break
            else:
                p = tree[p].daughter
    inner(tree, path, key)
    createavl(tree, start, key - 1)
    createavl(tree, key + 1, stop)


@cmd.addtoswitch(switch=handler.commands)
@iofiles(source='userdata.json', target='usertree.pkl')
@cmd.correctness
@cmd.addtoswitch(switch=handler.algorythms)
def genavl(handler: Handler, arr: list) -> str:
    """
    Converts list to AVL tree
    :param Toggle toggle:
    :param list arr:
    :return:
    :rtype: str
    """
    key = len(arr) // 2
    node = AVLnode(arr[key])
    arr.pop(key)
    arr.insert(0, node)
    createavl(arr, 1, len(arr) - 1)
    return 'AVL tree generated successfully'


@cmd.addtoswitch(switch=handler.commands)
@availability(toggle=handler.orders, name='methods')
@iofiles(source='usertree.pkl')
@cmd.correctness
def printtree(handler: Handler, tree: list, method: str, *, _e: bool = False) -> str:
    """
    Prints contents of the tree
    :param Handler handler:
    :param list tree:
    :param str method: User specified
    :param str _e: User specified, optional, extended node view, True or False
    :return: result
    :rtype: str
    """
    result = []
    if (iterator := handler.orders.get(method)) is None:
        return f'{method} method is not available'
    else:
        if _e:
            for key in iterator(tree, 0):
                result.append(f'{key} ' + repr(tree[key]))
        else:
            result.append('')
            for key in iterator(tree, 0):
                result[0] += f'{tree[key].value} '
        return '\n'.join(result)


@cmd.addtoswitch(switch=handler.kinds)
def lowest(tree: list, p: int = 0):
    if len(tree) == 0:
        return None
    while tree[p].son is not None:
        yield p
        p = tree[p].son
    yield p


@cmd.addtoswitch(switch=handler.kinds)
def largest(tree: list, p: int = 0):
    if len(tree) == 0:
        return None
    while tree[p].daughter is not None:
        yield p
        p = tree[p].daughter
    yield p


@cmd.addtoswitch(switch=handler.commands)
@iofiles(source='usertree.pkl')
@cmd.correctness
@cmd.addtoswitch(switch=handler.algorythms)
@availability(toggle=handler.kinds, name='methods')
def find(handler: Handler, tree: list, method: str) -> str:
    """
    Finds the lowest or the largest element
    :param Handler handler:
    :param list tree:
    :param str method: User specified
    :return: result
    :rtype: str
    """
    if (func := handler.kinds.get(method)) is not None:
        path = []
        for key in func(tree):
            path.append(repr(tree[key]))
        return '\n'.join(path)
    else:
        return f'{method} method is not available.'


def connect(tree: list, p: int, c: int, set: int):
    """
    Connects child with parent
    :param list tree:
    :param int p:
    :param int c:
    :param int set: 0 or 1
    :return:
    """
    if set == 0:
        tree[p].son = c
    else:
        tree[p].daughter = c


def deletebst(tree: list, key: int, p: int = 0) -> bool:
    """
    Delete a node
    :param list tree:
    :param int key:
    :param int p:
    :return: finished successfully
    :rtype: bool
    """
    parent = (0, 0)
    if tree[0] == key:
        if tree[0].son is None and tree[0].daughter is None:
            tree[0].value = None
        elif tree[0].son is None:
            tree[0].value = tree[tree[0].daughter].value
            tree[0].son = tree[tree[0].daughter].son
            tree[0].daughter = tree[tree[0].daughter].daughter
        elif tree[0].daughter is None:
            tree[0].value = tree[tree[0].son].value
            tree[0].daughter = tree[tree[0].son].daughter
            tree[0].son = tree[tree[0].son].son
        else:
            if tree[tree[0].daughter].son is None:
                tree[0].value = tree[tree[0].daughter].value
                tree[0].daughter = tree[tree[0].daughter].daughter
            else:
                s, sp = 0, 0
                for i in lowest(tree, p=tree[p].daughter):
                    sp = s
                    s = i
                tree[0].value = tree[s].value
                tree[sp].son = tree[s].daughter
        return True
    while True:
        if tree[p].value == key:
            if tree[p].son is None and tree[p].daughter is None:
                connect(tree, parent[0], None, parent[1])
            elif tree[p].son is None:
                connect(tree, parent[0], tree[p].daughter, parent[1])
            elif tree[p].daughter is None:
                connect(tree, parent[0], tree[p].son, parent[1])
            else:
                if tree[tree[p].daughter].son is None:
                    tree[p].value = tree[tree[p].daughter].value
                    tree[p].daughter = tree[tree[p].daughter].daughter
                else:
                    s, sp = 0, 0
                    for i in lowest(tree, p=tree[p].daughter):
                        sp = s
                        s = i
                    tree[p].value = tree[s].value
                    tree[sp].son = tree[s].daughter
            break
        elif key < tree[p].value and tree[p].son is not None:
            parent = (p, 0)
            p = tree[p].son
        elif tree[p].daughter is not None:
            parent = (p, 1)
            p = tree[p].daughter
        else:
            return False


def deleteavl(tree: list, key: int, p: int = 0) -> bool:
    """
    Delete a node
    :param list tree:
    :param int key:
    :param int p:
    :return: finished successfully
    :rtype: bool
    """
    parent = (0, 0)
    if tree[0] == key:
        if tree[0].son is None and tree[0].daughter is None:
            tree[0].value = None
        elif tree[0].son is None:
            tree[0].value = tree[tree[0].daughter].value
            tree[0].son = tree[tree[0].daughter].son
            tree[0].daughter = tree[tree[0].daughter].daughter
        elif tree[0].daughter is None:
            tree[0].value = tree[tree[0].son].value
            tree[0].daughter = tree[tree[0].son].daughter
            tree[0].son = tree[tree[0].son].son
        else:
            if tree[tree[0].daughter].son is None:
                tree[0].value = tree[tree[0].daughter].value
                tree[0].daughter = tree[tree[0].daughter].daughter
            else:
                s, sp = 0, 0
                for i in lowest(tree, p=tree[p].daughter):
                    tree[i].balance -= 1
                    sp = s
                    s = i
                tree[0].value = tree[s].value
                tree[sp].son = tree[s].daughter
            tree[p].balance += 1
        return True
    while True:
        if tree[p].value == key:
            if tree[p].son is None and tree[p].daughter is None:
                connect(tree, parent[0], None, parent[1])
            elif tree[p].son is None:
                connect(tree, parent[0], tree[p].daughter, parent[1])
            elif tree[p].daughter is None:
                connect(tree, parent[0], tree[p].son, parent[1])
            else:
                if tree[tree[p].daughter].son is None:
                    tree[p].value = tree[tree[p].daughter].value
                    tree[p].daughter = tree[tree[p].daughter].daughter
                else:
                    s, sp = 0, 0
                    for i in lowest(tree, p=tree[p].daughter):
                        tree[i].balance -= 1
                        sp = s
                        s = i
                    tree[p].value = tree[s].value
                    tree[sp].son = tree[s].daughter
                tree[p].balance += 1
            return True
        elif key < tree[p].value and tree[p].son is not None:
            parent = (p, 0)
            tree[p].balance -= 1
            p = tree[p].son
        elif tree[p].daughter is not None:
            parent = (p, 1)
            tree[p].balance += 1
            p = tree[p].daughter
        else:
            return False


@cmd.addtoswitch(switch=handler.commands, name='del')
@iofiles(source='usertree.pkl', target='usertree.pkl')
@cmd.correctness
def mydel(handler: Handler, tree: list, times: int) -> str:
    """
    Delete number of nodes
    :param Handler handler:
    :param list tree:
    :param int times: User specified, number of nodes to be deleted
    :return:
    :rtype: str
    """
    for _ in range(times):
        print('Enter key of the node to be deleted, or break to stop')
        key = 0
        while True:
            key = input().strip()
            if key == 'break':
                return 'Process canceled'
            try:
                key = int(key)
            except ValueError:
                print('Key must be an int')
            else:
                break
        if isinstance(tree[0], AVLnode):
            backup = copy.deepcopy(tree)
            if deleteavl(tree, key):
                balancer(tree)
                print('Node {key} succesfully deleted')
            else:
                tree = backup
                print('Node {key} doesn\'t exist')
        else:
            if deletebst(tree, key):
                print('Node {key} succesfully deleted')
            else:
                print('Node {key} doesn\'t exist')


def right(tree: list, p: int):
    """
    right
    :param list tree:
    :param int p:
    :return:
    """
    node = BSTnode(tree[p].value, tree[p].son, tree[p].daughter)
    pointer = tree[p].son
    tree[p].value = tree[pointer].value
    tree[p].son = tree[pointer].son
    tree[pointer].son = tree[pointer].daughter
    tree[pointer].daughter = node.daughter
    tree[pointer].value = node.value
    tree[p].daughter = pointer


def left(tree: list, p: int):
    """
    left
    :param list tree:
    :param int p:
    :return:
    """
    node = BSTnode(tree[p].value, tree[p].son, tree[p].daughter)
    pointer = tree[p].daughter
    tree[p].value = tree[pointer].value
    tree[p].daughter = tree[pointer].daughter
    tree[pointer].daughter = tree[pointer].son
    tree[pointer].son = node.son
    tree[pointer].value = node.value
    tree[p].son = pointer


@cmd.addtoswitch(switch=handler.commands)
@iofiles(source='usertree.pkl', target='usertree.pkl')
@cmd.correctness
@cmd.addtoswitch(switch=handler.algorythms)
def dsw(handler: Handler, tree: list) -> str:
    """
    Balance bst tree
    :param Handler handler:
    :param Handler tree:
    :return:
    :rtype: str
    """
    if isinstance(tree[0], AVLnode):
        return 'Tree must contain BST nodes only.'
    p = 0
    l = 0
    while p is not None:
        if tree[p].son is not None:
            right(tree, p)
        else:
            p = tree[p].daughter
            l += 1
    p = 0
    m = 2**(int(math.log(l + 1, 2))) - 1
    for _ in range(l - m):
        left(tree, p)
        p = tree[p].daughter
    while m > 1:
        p = 0
        m //= 2
        for _ in range(m):
            left(tree, p)
            p = tree[p].daughter
    return 'dsw finished successfully'


if __name__ == '__main__':
    if not os.path.isfile('settings.json'):
        jsonwrite({'upperlimit': 100,
                   'upperlimit!':'Lenght of the longest list to be generated, \
must be a multiple of 10, must be higher than 10.'}, 'settings.json')
    if not os.path.isdir('data'):
        os.mkdir('data')
    if not os.path.isdir('processeddata'):
        os.mkdir('processeddata')
    if not os.path.isdir('figures'):
        os.mkdir('figures')
    sys.setrecursionlimit(10**6)
    print('Forester by Jakub Błażejowski', 'Type list to see the list of available commands.', sep='\n')
    cmd.main(handler)