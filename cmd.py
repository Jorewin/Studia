import types
import functools
import re
import sys
import os


class Controller():
    def __init__(self):
        self.commands = {}


controller= Controller()


def addtoswitch(_func: types.FunctionType = None,* , switch: dict = None, name: str = None) -> types.FunctionType:
    """
    Adds function to pointed switch

    :param _func: Any not built-in python function.
    :type _func: types.FunctionType or None
    :param dict switch:
    :param name:
    :type name: str or None
    :return: input function
    :rtype: types.FunctionType
    :raises TypeError: if any of given arguments is of the wrong type
    """
    def decorator_addtoswitch(func: types.FunctionType) -> types.FunctionType:
        if not isinstance(switch, dict):
            raise TypeError(f'Switch must be a dictionary, not a {type(switch)}.')
        if name is None:
            switch[func.__name__] = func
        elif isinstance(name, str):
            switch[name] = func
        else:
            raise TypeError(f'Name must be a string, not a {type(name)}.')
        return func
    if _func is None:
        return decorator_addtoswitch
    else:
        return decorator_addtoswitch(_func)


def correctness(func: types.FunctionType) -> types.FunctionType:
    """
    Checks if all args and kwargs are of the right type (Function must have annotations for this to work)
    :param types.FunctionType func:
    :return:
    :rtype: types.FunctionType
    """
    @functools.wraps(func)
    def wrapper_correctness(*args, **kwargs):
        checklist = {arg: 0 for arg in func.__annotations__}
        for kwarg in kwargs:
            if (_type := func.__annotations__.get(kwarg)) is None:
                print(f'{func.__name__} got an unexpected argument {kwarg}')
                break
            if not isinstance(kwargs[kwarg], _type):
                print(f'{func.__name__} {kwarg} must be a {_type}, not a {type(kwargs[kwarg])}.')
                break
            checklist[kwarg] = 1
        else:
            if func.__kwdefaults__ is not None:
                for kwarg in func.__kwdefaults__:
                    checklist[kwarg] = 1
            counter = 0
            for arg in checklist:
                if checklist[arg] == 1:
                    continue
                if counter >= len(args):
                    print(f'{func.__name__}, missing argument {arg}')
                    break
                if not isinstance(args[counter], func.__annotations__[arg]):
                    print(f'{func.__name__} {arg} must be a {func.__annotations__[arg]}, not a {type(args[counter])}')
                    break
                counter += 1
            else:
                if counter == len(args):
                    func(*args, **kwargs)
                else:
                    print(f'{func.__name__}, too many arguments were given')
    return wrapper_correctness


@addtoswitch(switch=controller.commands, name='list')
@correctness
def clist(controller: Controller):
    """
    Used to generate list of available commands
    :param Controller controller:
    :return:
    """
    print('Available commands:')
    for command in controller.commands:
        print(f'\t+ {command:20} -> {controller.commands[command].__name__}')
    print('Type help [command_name] to get more info about specific command')


@addtoswitch(switch=controller.commands, name='exit')
@correctness
def cexit(controller: Controller):
    """
    Terminates the process
    :param Controller controller:
    :return:
    """
    print('Process terminated')
    sys.exit()


@addtoswitch(switch=controller.commands, name='help')
@correctness
def chelp(controller: Controller, command: str = None):
    """
    Shows documentation of the chosen command
    :param Controller controller:
    :param command: User specified
    :type command: None or str
    :return:
    """
    if command is None:
        print('Type help [command_name] to get more info about specific command')
    elif (func := controller.commands.get(command)) is not None:
        print(f'''{command} command
Usage: command, params marked as user specified, optional params in format [name] value
Example: printtree in_order _e True''')
        print(func.__doc__)
    else:
        print(f'Command {command} is not an available command, type list to see the list of available commands')


@addtoswitch(switch=controller.commands, name='clear')
@correctness
def cclear(controller: Controller):
    """
    Clear the screen
    :param Controller controller:
    :return:
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def detector(charray: str):
    """
    Convert string to int or list if possible
    :param str charray:
    :return:
    """
    if charray == 'False':
        return False
    if charray == 'True':
        return True
    if re.match('\[([0-9]+,)*[0-9]+\]', charray):
        arr = [int(i) for i in re.findall('[0-9]+', charray)]
        return arr
    try:
        value = int(charray)
    except ValueError:
        pass
    else:
        return value
    return charray


def main(controller: Controller):
    """
    Terminal handler
    :param Controller controller:
    :return:
    """
    while True:
        print('>> ', end='')
        data = input().strip().split()
        for i in range(len(data)-1, -1, -1):
            if data[i] == ' ':
                del data[i]
        if len(data) == 0:
            continue
        kwarguments = {}
        for i in range(len(data) - 1, -1, -1):
            if match := re.match('^_.$', data[i]):
                del data[i]
                try:
                    kwarguments[match.string] = detector(data[i])
                    del data[i]
                except KeyError:
                    print(f'{match.string} value not found.')
        command, *arguments = data
        arguments = [detector(argument) for argument in arguments]
        if (func := controller.commands.get(command.lower())) is not None:
            func(controller, *arguments, **kwarguments)
        else:
            print(f'{command} is not a defined command')


if __name__ == '__main__':
    print(addtoswitch.__annotations__)
