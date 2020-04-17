import cmd
import numpy
import random
import os.path
import json
import functools
import types
import pickle
import re


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
    def __init__(self, balance = 0):
        self.balance = balance
        super().__init__()


    def __repr__(self):
        return f'AVLnode value: {self.value}, son: {self.son}, daughter: {self.daughter}, bf: {self.balance}'


handler = Handler()
handler.commands = cmd.controller.commands


def use_userdata(_func: types.FunctionType = None, *, source: str = None, target: str = None):
    """
    Makes algorythm use arr from userdata.json
    :param types.FunctionType func:
    :param str source: source file
    :param str target: target file
    :return: decorated function
    :rtype: types.FunctionType
    """
    def decorator_use_userdata(func):
        @functools.wraps(func)
        def wrapper_use_userdata(handler: Handler, *args, **kwargs):
            if not os.path.isfile(source):
                print('Generate or enter the data first.')
                return
            if (_type := re.search('\.[A-z]+', source)) is None:
                print('File without extension')
                return
            if handler.readmodes.get(_type.group()) is None:
                print(f'{_type.group()} extension is not available')
                return
            data = handler.readmodes[_type.group()](source)
            func(handler, data, *args, **kwargs)
            if target is not None:
                if (_type := re.search('\.[A-z]+', target)) is None:
                    print('File without extension')
                if handler.writemodes.get(_type.group()) is None:
                    print(f'{_type.group()} extension is not available')
                handler.writemodes[_type.group()](data, target)
        return wrapper_use_userdata
    if _func is None:
        return decorator_use_userdata
    else:
        return decorator_use_userdata(_func)


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
    Read from json file
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
        json.dump(object, target)


@cmd.addtoswitch(switch=handler.commands)
@cmd.correctness
def enterdata(handler: Handler, arr: list):
    """
    Lets user input list into the system
    :param Handler handler:
    :param list arr: User specified, example [1,2,3,4,5]
    :return:
    """
    with open('userdata.json', 'w') as target:
        json.dump(arr, target)
    print('Data saved successfully')


@cmd.addtoswitch(switch=handler.commands)
@cmd.correctness
def gendata(handler: Handler, lenght: int):
    """
    Generates test arr
    :param Toggle toggle:
    :param int lenght: User specified
    :return:
    """
    if lenght < 0:
        print('Lenght must be a nonnegative integer')
        return
    arr = [random.randint(0, lenght+1) for _ in range(lenght)]
    with open('userdata.json', 'w') as target:
        json.dump(arr, target)
    print('Data saved successfully')


@cmd.addtoswitch(switch=handler.commands)
@cmd.correctness
def printdata(handler: Handler):
    """
    Prints data from userdata.json if the file exists
    :param Handler handler:
    :return:
    """
    if not os.path.isfile('userdata.json'):
        print('Generate or enter the data first.')
        return
    with open('userdata.json', 'r') as source:
        print(json.load(source))


@cmd.addtoswitch(switch=handler.orders)
def pre_order(tree: list, p: int):
    """
    Yields keys of the tree
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
def in_order(tree: list, p: int):
    """
    Yields keys of the tree
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
@use_userdata(source='userdata.json', target='usertree.pkl')
@cmd.addtoswitch(switch=handler.algorythms)
def genbst(handler: Handler, arr: list):
    """
    Converts list to BST tree
    :param Toggle toggle:
    :param list arr:
    :return:
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
    print('Tree generated successfully')


@cmd.addtoswitch(switch=handler.commands)
@use_userdata(source='userdata.json', target='usertree.pkl')
@cmd.addtoswitch(switch=handler.algorythms)
def genavl(handler: Handler, arr: list):
    """
    Converts list to BST tree
    :param Toggle toggle:
    :param list arr:
    :return:
    """
    for key in range(len(arr)):
        node = AVLnode(arr[key])
        arr[key] = node
        if key == 0:
            continue
        p = 0
        while True:
            if arr[key].value < arr[p].value:
                arr[p].balance += 1
                if arr[p].son is None:
                    arr[p].son = key
                    break
                else:
                    p = arr[p].son
            else:
                arr[p].balance -= 1
                if arr[p].daughter is None:
                    arr[p].daughter = key
                    break
                else:
                    p = arr[p].daughter
        for p in in_order(arr, 0):
            if arr[p].balance < -1:
                if arr[arr[p].daughter].balance >= 0:
                    pass

    print('Tree generated successfully')


@cmd.addtoswitch(switch=handler.commands)
@availability(toggle=handler.orders, name='methods')
@use_userdata(source='usertree.pkl')
@cmd.correctness
def printtree(handler: Handler, tree: list, method: str):
    """
    Prints contents of the tree
    :param Handler handler:
    :param list tree:
    :param str method: User specified
    :return:
    """
    if (iterator := handler.orders.get(method)) is None:
        print(f'{method} method is not available')
    else:
        for key in iterator(tree, 0):
            print(tree[key].value, end=' ')
        print('\nDone')


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
@availability(toggle=handler.kinds, name='methods')
@use_userdata(source='usertree.pkl')
@cmd.correctness
def find(handler: Handler, tree: list, method: str):
    """
    Finds the lowest or the largest element
    :param Handler handler:
    :param list tree:
    :param str method: User specified
    :return:
    """
    if (func := handler.kinds.get(method)) is not None:
        path = ''
        for key in func(tree):
            path += repr(tree[key]) + '\n'
        print(path)
    else:
        print(f'{method} method is not available.')


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


def delete(tree: list, key: int, p: int = 0):
    """
    Delete a node
    :param list tree:
    :param int key:
    :param int p:
    :return:
    """
    parent = (0, 0)
    while True:
        if tree[p].value == key:
            if tree[p].son is None and tree[p].daughter is None:
                connect(tree, parent[0], None, parent[1])
            elif tree[p].son is None:
                connect(tree, parent[0], tree[p].daughter, parent[1])
            elif tree[p].daughter is None:
                connect(tree, parent[0], tree[p].son, parent[1])
            else:
                s = lowest(tree, p=tree[p].daughter)[-1]
                sp = lowest(tree, p=tree[p].daughter)[-2]
                tree[p].value = tree[s].value
                delete(tree, tree[s].value, sp)
            break
        elif key < tree[p].value and tree[p].son is not None:
            parent = (p, 0)
            p = tree[p].son
        elif tree[p].daughter is not None:
            parent = (p, 1)
            p = tree[p].daughter
        else:
            print(f'There is no node with given {key} key')
            break


@cmd.addtoswitch(switch=handler.commands, name='del')
@use_userdata(source='usertree.pkl', target='usertree.pkl')
@cmd.correctness
def mydel(handler: Handler, tree: list, times: int):
    """
    Delete number of nodes
    :param Handler handler:
    :param list tree:
    :param int times: User specified, number of nodes to be deleted
    :return:
    """
    for _ in range(times):
        print('Enter key of the node to be deleted')
        key = 0
        while True:
            try:
                key = int(input().strip())
            except ValueError:
                print('Key must be an int')
            else:
                break
        delete(tree, key)


if __name__ == '__main__':
    print('Forester by Jakub Błażejowski', 'Type list to see the list of available commands.', sep='\n')
    cmd.main(handler)