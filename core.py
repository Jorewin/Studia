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
        super().__init__()


class BSTnode():
    def __init__(self, value: int, son: int = None, daughter: int = None):
        self.value = value
        self.son = son
        self.daughter = daughter


    def __repr__(self):
        return f'BSTnode value: {self.value}, son: {self.son}, daughter: {self.daughter}'


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
    :param list arr: example [1,2,3,4,5]
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
    :param int lenght:
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


@cmd.addtoswitch(switch=handler.orders)
def pre_order(tree, p: int):
    """
    Yields keys of the tree
    :param arr:
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
def in_order(tree, p: int):
    """
    Yields keys of the tree
    :param arr:
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
def post_order(tree, p: int):
    """
    Yields keys of the tree
    :param arr:
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
@availability(toggle=handler.orders, name='methods')
@use_userdata(source='usertree.pkl')
@cmd.correctness
def printtree(handler: Handler, tree: list, method: str):
    """
    Prints contents of the tree
    :param Handler handler:
    :param list tree:
    :param str method:
    :return:
    """
    if (iterator := handler.orders.get(method)) is None:
        print(f'{method} method is not available')
    else:
        for key in iterator(tree, 0):
            print(tree[key].value, end=' ')
        print('\nDone')


def lowest(tree: list):
    if len(tree) == 0:
        return None
    path = ''
    p = 0
    while tree[p].son is not None:
        path += repr(tree[p]) + '\n'
        p = tree[p].son
    path += repr(tree[p]) + '\n'
    return path


def largest(tree: list):
    if len(tree) == 0:
        return None
    path = ''
    p = 0
    while tree[p].daughter is not None:
        path += repr(tree[p]) + '\n'
        p = tree[p].daughter
    path += repr(tree[p]) + '\n'
    return path


@cmd.addtoswitch(switch=handler.commands)
@use_userdata(source='usertree.pkl')
@cmd.correctness
def find(handler: Handler, tree: list, method: str):
    """
    Finds the lowest or the largest element
    :param Handler handler:
    :param list tree:
    :param str method:
    :return:
    """
    if method == 'lowest':
        print(lowest(tree))
    elif method == 'largest':
        print(largest(tree))
    else:
        print(f'{method} method is not available.')


if __name__ == '__main__':
    print('Forester by Jakub Błażejowski', 'Type list to see the list of available commands.', sep='\n')
    cmd.main(handler)