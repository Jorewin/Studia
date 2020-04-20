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
            print(f'{func.__name__} finished successfully')
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
    p = 0
    while True:
        if tree[key].value < tree[p].value:
            tree[p].balance += 1
            if tree[p].son is None:
                tree[p].son = key
                break
            else:
                p = tree[p].son
        else:
            tree[p].balance -= 1
            if tree[p].daughter is None:
                tree[p].daughter = key
                break
            else:
                p = tree[p].daughter
    balancer(tree)
    createavl(tree, start, key - 1)
    createavl(tree, key + 1, stop)


@cmd.addtoswitch(switch=handler.commands)
@use_userdata(source='userdata.json', target='usertree.pkl')
@cmd.addtoswitch(switch=handler.algorythms)
def genavl(handler: Handler, arr: list):
    """
    Converts list to AVL tree
    :param Toggle toggle:
    :param list arr:
    :return:
    """
    key = len(arr) // 2
    node = AVLnode(arr[key])
    arr.pop(key)
    arr.insert(0, node)
    createavl(arr, 1, len(arr) - 1)


@cmd.addtoswitch(switch=handler.commands)
@availability(toggle=handler.orders, name='methods')
@use_userdata(source='usertree.pkl')
@cmd.correctness
def printtree(handler: Handler, tree: list, method: str, *, _e: str = 'no'):
    """
    Prints contents of the tree
    :param Handler handler:
    :param list tree:
    :param str method: User specified
    :param str _e: User specified, optional, extended node view, yes or no
    :return:
    """
    if (iterator := handler.orders.get(method)) is None:
        print(f'{method} method is not available')
    else:
        if _e == 'yes':
            for key in iterator(tree, 0):
                print(f'{key}', repr(tree[key]))
        else:
            for key in iterator(tree, 0):
                print(tree[key].value, end=' ')


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


def deletebst(tree: list, key: int, p: int = 0):
    """
    Delete a node
    :param list tree:
    :param int key:
    :param int p:
    :return:
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
        return
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
            print(f'There is no node with given {key} key')
            break


def deleteavl(tree: list, key: int, p: int = 0):
    """
    Delete a node
    :param list tree:
    :param int key:
    :param int p:
    :return:
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
            print(f'There is no node with given {key} key')
            return False


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
        if isinstance(tree[0], AVLnode):
            backup = copy.deepcopy(tree)
            if deleteavl(tree, key):
                balancer(tree)
            else:
                tree = backup
        else:
            deletebst(tree, key)


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
@use_userdata(source='usertree.pkl', target='usertree.pkl')
@cmd.correctness
@cmd.addtoswitch(switch=handler.algorythms)
def dsw(handler: Handler, tree: list):
    """
    Balance bst tree
    :param Handler handler:
    :param Handler tree:
    :return:
    """
    if isinstance(tree[0], AVLnode):
        print('Tree must contain BST nodes only.')
        return
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


if __name__ == '__main__':
    print('Forester by Jakub Błażejowski', 'Type list to see the list of available commands.', sep='\n')
    cmd.main(handler)